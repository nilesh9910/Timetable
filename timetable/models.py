from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

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
    no_of_lec = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(14)])
    def __str__(self):
        return self.name

class Subject(models.Model):
    name_of_sub = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='all_sub')
    def __str__(self):
        return f'{self.name_of_sub}'    

class SubjectCell(models.Model):
    day = models.IntegerField(choices = DayChoice.choices)
    of_time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name='sub_cell')
    period = models.IntegerField(validators=[MaxValueValidator(14)])
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="cell")

    