# model.py class contains essential fields and behaviour of data you're storing
# model is a Python class that subclasses django.db.models.Model.

from django.db import models

# Django automatically gives you a database-abstraction API that lets you 
# create, retrieve, update and delete objects after you've created data models.

"""
Round System :

1.PenPaperRound
2.TaskRoundOne
3.TaskRoundTwo
4.GroupDiscussionRound
5.FinalRound

"""

# PenPaperRound would create a database for storing the fields and is same for other classes. 
# pi_taken_by, pi_review and pi_task are fields.
# Each field takes a certain set of field-specific-requirements to work.

# CharField denotes the data types.max_length represent maximum length of string
# if null=True Django will store empty values as NULL in the database. Default is False.
# if blank=True then the field is allowed to be empty. Default is false.

class PenPaperRound(models.Model):
    pi_taken_by = models.CharField(max_length=255)
    pi_review = models.CharField(max_length=255)
    pi_task = models.CharField(max_length=255, null=True, blank=True)

    # method to return the values
    def __str__(self):
        return str(self.pk)

# BooleanField in task_done denotes True or False values it can store.
# False is resulted if audition is stopped by admin or the student is inducted.

class TaskRoundOne(models.Model):
    task_desc = models.CharField(max_length=255)
    task_given_by = models.CharField(max_length=255)
    task_submission_date = models.CharField(max_length=255)
    task_review = models.CharField(max_length=255)
    task_done = models.BooleanField()

    def __str__(self):
        return str(self.pk)

# class to get data for second round task

class TaskRoundTwo(models.Model):
    task_desc = models.CharField(max_length=255)
    task_given_by = models.CharField(max_length=255)
    task_submission_date = models.CharField(max_length=255)
    task_review = models.CharField(max_length=255)
    task_done = models.BooleanField()

    def __str__(self):
        return str(self.pk)
        

class GroupDiscussionRound(models.Model):
    gd_review = models.CharField(max_length=255)
    gd_taken_by = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)


class FinalPi(models.Model):
    pi_taken_by = models.CharField(max_length=255)
    pi_review = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)

# ForeignKey offers database relationship.
# ForeignKey requires a positional argument: the class to which the model is related.
# on_delete=models.CASCADE.When the referenced object is deleted,also delete the objects that have references to it 
# null=True implies store empty values as NULL. 
# blank=True allows field to be empty.

class Student(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    dept = models.CharField(max_length=20)
    pen_paper_round = models.ForeignKey(PenPaperRound, on_delete=models.CASCADE, null=True, blank=True)
    task_round_one = models.ForeignKey(TaskRoundOne, on_delete=models.CASCADE, null=True, blank=True)
    task_round_two = models.ForeignKey(TaskRoundTwo, on_delete=models.CASCADE, null=True, blank=True)
    gd_round = models.ForeignKey(GroupDiscussionRound, on_delete=models.CASCADE, null=True, blank=True)
    final_pi = models.ForeignKey(FinalPi, on_delete=models.CASCADE, null=True, blank=True)
    current_round = models.IntegerField(default=1)
    stopped = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    # returning the name of student in the above method

# class AppConfig for enabling the viewing of results to all users 

class AppConfig(models.Model):
    show_results = models.BooleanField(default=False)

    def __str__(self):
        return str(self.show_results)
        