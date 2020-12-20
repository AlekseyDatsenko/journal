from django.views.generic import ListView
from django.shortcuts import render, redirect
from . import models
from . forms import MonthMark
from django.contrib.auth import get_user_model


class PupilListView(ListView):

    def get_queryset(self):
        if self.request.user not in models.ClassroomTeacher.objects.all():
            grades_list = models.PupilMonthMarks.objects.filter(pupil=self.request.user)
        return grades_list

    template_name = 'grades_list_pupil.html'


class ClassroomTeacherListView(ListView):
    model = models.PupilMonthMarks
    template_name = 'grades_list_teacher.html'


def new_marks(request):
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'POST':
        form = MonthMark(request.POST)
        if form.is_valid():
            user_marks = form.save(commit=False)
            user_marks.save()
            return redirect('new_marks')
    else:
        form = MonthMark()
    return render(request, 'new_marks.html', {'form': form, 'users': users})
