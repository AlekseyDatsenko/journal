from django.urls import path
from . import views

urlpatterns = [
    path('', views.PupilListView.as_view(), name='grades_list_pupil'),
    path('teacher', views.ClassroomTeacherListView.as_view(), name='grades_list_teacher'),
    path('new', views.new_marks, name='new_marks'),
]
