from django.contrib import admin
from .models import TimeTable, SubjectCell, Subject
# Register your models here.

admin.site.register(TimeTable)
admin.site.register(SubjectCell)
admin.site.register(Subject)