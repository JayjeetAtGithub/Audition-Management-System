from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

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


def dashboard(request):
    students = Student.objects.all()
    for student in students:
        student.current_round = round_details[student.current_round]
    context_data = {
        'students': students,
    }
    return render(request, 'dashboard.html', context_data)


def profile(request, id):
    student_details = Student.objects.filter(id=id).first()
    if request.method == 'POST':
        if student_details.current_round <= 6:
            messages.error(request, 'Student Already Inducted !')
            return redirect('/profile/{}'.format(int(id)))
        else:
            student_details.current_round = student_details.current_round + 1
            student_details.save()
            return redirect('/dashboard')
    else:
        student_details.current_round = round_details[student_details.current_round]
        context_data = {
            'student_details': student_details,
        }
        return render(request, 'profile.html', context_data)
