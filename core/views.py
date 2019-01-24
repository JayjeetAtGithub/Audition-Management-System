from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, AppConfig

round_details = {
    1: 'Pen and Paper Round',
    2: 'Task Round One',
    3: 'Task Round Two',
    4: 'Group Discussion Round',
    5: 'Final Personal Interview',
    6: 'Inducted'
}


def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    students = Student.objects.all()
    for student in students:
        student.current_round = round_details[student.current_round]
    context_data = {
        'students': students,
    }
    return render(request, 'dashboard.html', context_data)


@login_required
def profile(request, id):
    student_details = Student.objects.filter(id=id).first()
    student_details.current_round = round_details[student_details.current_round]
    context_data = {
        'student_details': student_details,
    }
    return render(request, 'profile.html', context_data)


@login_required
def promote(request, id):
    if request.method == 'POST':
        student_details = Student.objects.filter(id=id).first()
        if student_details.current_round < 6:
            student_details.current_round = student_details.current_round + 1
            student_details.save()
            return redirect('/dashboard')
        else:
            messages.error(request, 'Already Inducted')
            return redirect('/profile/{}'.format(int(id)))


@login_required
def stop(request, id):
    if request.method == 'POST':
        student_details = Student.objects.filter(id=id).first()
        student_details.stopped = True
        student_details.save()
        return redirect('/dashboard')


@login_required
def resume(request, id):
    if request.method == 'POST':
        student_details = Student.objects.filter(id=id).first()
        student_details.stopped = False
        student_details.save()
        return redirect('/dashboard')


def results(request):
    students = Student.objects.all()
    config = AppConfig.objects.get(id=1)
    for student in students:
        student.current_round = round_details[student.current_round]
    context_data = {
        'students': students,
        'result_status': config.show_results,
    }
    return render(request, 'results.html', context_data)


@login_required
def set_result_status(request):
    config = AppConfig.objects.get(id=1)
    config.show_results = not config.show_results
    config.save()
    return redirect('/dashboard')
