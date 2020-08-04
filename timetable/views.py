from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
import datetime
from .models import DayChoice
from .forms import TimeTableForm
# Create your views here.
def index(request):
    form = TimeTableForm()
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('timetable:edit', args=(obj.id,)))
        else:
            return render(request, 'timetable/index.html', {'form': form, 'error': True})
    ctx = {'form': form}
    return render(request, 'timetable/index.html',ctx)

def edit(request, id):
    return render(request, 'timetable/edit.html', {'id': id})

# def index(request):
#     e = list()
#     f = request.user.all_timetable.all()[0].starts_at
#     print(f)
#     for _ in range(request.user.all_timetable.all()[0].no_of_lec):
#         print(f)
#         g = datetime.datetime.combine(datetime.date.today(), f)+datetime.timedelta(minutes=request.user.all_timetable.all()[0].duration_of_each_lec)
#         e.append(f'{f} - {g.time()}')
#         f = g.time()
#     c = list()
#     for _ in range(7):
#         d=list()
#         for _ in range(request.user.all_timetable.all()[0].no_of_lec):
#             d.append(None)
#         c.append(d)
#     for cell in request.user.all_timetable.all()[0].sub_cell.all():
#         c[cell.day][cell.period]=cell.subject_set.get().name_of_sub
#     print(type(request.user.all_timetable.all()[0].starts_at))
#     i = [DayChoice(j).label for j in range(7)]
#     mylist = zip(c, i)
#     # t = request.user.all_timetable.all()[0].starts_at
#     # n_t = datetime.datetime.combine(datetime.date.today(), t)+datetime.timedelta(minutes=90)
#     # print(n_t.time())

#     ctx = {'timet': request.user.all_timetable.all()[0].sub_cell.all(),  'f': request.user.all_timetable.all()[0].starts_at, 'e': e, 'mylist': mylist}
#     return render(request, 'timetable/index.html', ctx)