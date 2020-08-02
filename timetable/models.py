from django.db import models
from django.conf import settings

# Create your models here.
class DayChoice(models.IntegerChoices):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class TimeTable(models.Model):
    name = models.CharField(max_length=30)
    duration_of_each_lec = models.IntegerField()
    day_off = models.IntegerField(choices = DayChoice.choices, null=True, blank=True)
    starts_at = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='all_timetable')
    def __str__(self):
        return self.name
    

class SubjectCell(models.Model):
    day = models.IntegerField(choices = DayChoice.choices)
    of_time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name='sub_cell')

class Subject(models.Model):
    name_of_sub = models.CharField(max_length=30)
    cells = models.ForeignKey(SubjectCell, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name_of_sub}'
    