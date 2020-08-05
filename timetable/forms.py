from django import forms
from .models import TimeTable, Subject, SubjectCell
from django.utils.translation import gettext_lazy as _

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['name', 'duration_of_each_lec', 'day_off', 'starts_at', 'no_of_lec']
        labels = {
            'day_off': _('Holiday on')
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
        fields = ['day', 'period']