from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta, date
from .models import DayChoice, TimeTable
from .forms import TimeTableForm
from django.views.generic import ListView
# Create your views here.
def index(request):
    form = TimeTableForm()
    ctx = {'form': form}
    if request.user.is_authenticated:
        ctx["all_timetable"] = TimeTable.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('timetable:edit', args=(obj.id,)))
        else:
            ctx["form"]=form
            ctx["error"]=True
            return render(request, 'timetable/index.html', ctx)
    
    return render(request, 'timetable/index.html',ctx)

def edit(request, id):
    # get the timetable which is to be edited from data base
    this_timetable = request.user.all_timetable.filter(id=id)[0]

    # getting time head which the timing of lecture start and end
    time_head = list()
    starts_at = this_timetable.starts_at
    for _ in range(this_timetable.no_of_lec):
        n_dtime = datetime.combine(date.today(), starts_at) + timedelta(minutes=this_timetable.duration_of_each_lec)
        time_head.append(f'{starts_at} - {n_dtime.time()}')
        starts_at = n_dtime.time()
    
    # creating a two dimension list with subject name if there is a lecture added else None 
    list_tt = [[None for _ in range(this_timetable.no_of_lec)] for _ in range(7)]
    for cell in this_timetable.sub_cell.all():
        list_tt[cell.day][cell.period] = cell.subject_set.get().name_of_sub
    
    # get all days in the choices available
    all_days = [DayChoice(j).label for j in range(7)]
    mylist = zip(list_tt, all_days)
    return render(request, 'timetable/edit.html', {'id': id, 'mylist': mylist, 'time_head': time_head})