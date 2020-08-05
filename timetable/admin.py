from django.contrib import admin
from .models import TimeTable, SubjectCell, Subject
# Register your models here.

class SubjectCellInLine(admin.TabularInline):
    model = SubjectCell
    extra = 1

class TimeTableAdmin(admin.ModelAdmin):
    inlines = [
        SubjectCellInLine,
    ]


admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(SubjectCell)
admin.site.register(Subject)