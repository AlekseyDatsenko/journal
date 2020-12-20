from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class ClassroomTeacher(models.Model):
    classroom_teacher = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.classroom_teacher.username


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=15)

    def __str__(self):
        return self.lesson_name


class MonthName(models.Model):
    month_name = models.CharField(max_length=15)

    def __str__(self):
        return self.month_name


class PupilMonthMarks(models.Model):
    pupil = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    month_name = models.ForeignKey(MonthName, on_delete=models.CASCADE)
    mark_1 = models.CharField(max_length=8, blank=True)
    mark_2 = models.CharField(max_length=8, blank=True)
    mark_3 = models.CharField(max_length=8, blank=True)
    mark_4 = models.CharField(max_length=8, blank=True)
    mark_5 = models.CharField(max_length=8, blank=True)
    mark_6 = models.CharField(max_length=8, blank=True)
    mark_7 = models.CharField(max_length=8, blank=True)
    mark_8 = models.CharField(max_length=8, blank=True)
    mark_9 = models.CharField(max_length=8, blank=True)
    mark_10 = models.CharField(max_length=8, blank=True)
    mark_11 = models.CharField(max_length=8, blank=True)
    mark_12 = models.CharField(max_length=8, blank=True)
    mark_13 = models.CharField(max_length=8, blank=True)
    mark_14 = models.CharField(max_length=8, blank=True)
    mark_15 = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return self.pupil.username
