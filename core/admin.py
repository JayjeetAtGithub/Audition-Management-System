from django.contrib import admin
from .models import FinalPi, Student, TaskRoundOne, TaskRoundTwo, GroupDiscussionRound, PenPaperRound


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'stopped', 'current_round', 'year', 'dept')


admin.site.register(Student, StudentAdmin)
admin.site.register(TaskRoundOne)
admin.site.register(TaskRoundTwo)
admin.site.register(GroupDiscussionRound)
admin.site.register(PenPaperRound)
admin.site.register(FinalPi)
