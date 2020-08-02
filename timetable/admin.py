from django.contrib import admin
from .models import TimeTable, SubjectCell, Subject
# Register your models here.

class SubjectCellInLine(admin.TabularInline):
    model = SubjectCell
    extra = 1

class SubjectInLine(admin.TabularInline):
    model = Subject
    extra = 1

class TimeTableAdmin(admin.ModelAdmin):
    inlines = [
        SubjectCellInLine,
    ]
class SubjectCellAdmin(admin.ModelAdmin):
    inlines = [
        SubjectInLine,
    ]


admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(SubjectCell, SubjectCellAdmin)
admin.site.register(Subject)