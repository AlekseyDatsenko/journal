from django import forms
from django.contrib.auth import get_user_model
from . models import PupilMonthMarks


class MonthMark(forms.ModelForm):

    class Meta:
        model = PupilMonthMarks
        fields = ('pupil', 'lesson', 'month_name', 'mark_1',
                  'mark_2', 'mark_3', 'mark_4', 'mark_5',
                  'mark_6', 'mark_7', 'mark_8', 'mark_9',
                  'mark_10', 'mark_11', 'mark_12', 'mark_13',
                  'mark_14', 'mark_15')
