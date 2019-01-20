from django.db import models


class PenPaperRound(models.Model):
    pi_taken_by = models.CharField(max_length=255)
    pi_review = models.CharField(max_length=255)
    pi_task = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class GroupDiscussionRound(models.Model):
    gd_review = models.CharField(max_length=255)
    gd_taken_by = models.CharField(max_length=255)
    promote = models.BooleanField()

    def __str__(self):
        return str(self.pk)


class TaskRoundOne(models.Model):
    task_desc = models.CharField(max_length=255)
    task_given_by = models.CharField(max_length=255)
    task_submission_date = models.CharField(max_length=255)
    task_review = models.CharField(max_length=255)
    task_done = models.BooleanField()
    promote = models.BooleanField()

    def __str__(self):
        return str(self.pk)


class TaskRoundTwo(models.Model):
    task_desc = models.CharField(max_length=255)
    task_given_by = models.CharField(max_length=255)
    task_submission_date = models.CharField(max_length=255)
    task_review = models.CharField(max_length=255)
    task_done = models.BooleanField()
    promote = models.BooleanField()

    def __str__(self):
        return str(self.pk)


class FinalPi(models.Model):
    pi_taken_by = models.CharField(max_length=255)
    pi_review = models.CharField(max_length=255)
    promote = models.BooleanField()

    def __str__(self):
        return int(self.pk)


class Student(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    dept = models.CharField(max_length=20)
    pen_paper_round = models.ForeignKey(
        PenPaperRound, on_delete=models.CASCADE, null=True, blank=True)
    task_round_one = models.ForeignKey(
        TaskRoundOne, on_delete=models.CASCADE, null=True, blank=True)
    task_round_two = models.ForeignKey(
        TaskRoundTwo, on_delete=models.CASCADE, null=True, blank=True)
    gd_round = models.ForeignKey(
        GroupDiscussionRound, on_delete=models.CASCADE, null=True, blank=True)
    final_pi = models.ForeignKey(
        FinalPi, on_delete=models.CASCADE, null=True, blank=True)

    current_round = 0

    def evaluate_current_round(self):
        pass

    def __str__(self):
        return self.name
