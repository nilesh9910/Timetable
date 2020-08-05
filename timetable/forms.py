from django import forms
from .models import TimeTable, Subject, SubjectCell
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import widgets 

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['name', 'duration_of_each_lec', 'day_off', 'starts_at', 'no_of_lec']
        labels = {
            'day_off': _('Holiday on')
        }
        labels = {
            'starts_at': 'Starting Time of First Lecture (hh:mm) eg.05:00 '
        }
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name_of_sub']
        labels = {
            'name_of_sub': 'Name of Subject'
        }
class SubjectCellForm(forms.ModelForm):
    class Meta:
        model = SubjectCell
        fields = ['subject', 'day', 'period']
        