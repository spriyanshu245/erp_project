from django.shortcuts import render, HttpResponseRedirect
from .forms import AddStudentNew, AddProEvent, AddStudPart5, AddStartUp6
from .models import StudentNew, ProEvent, DeptStudPart5, FacultyDevProOrg_Dep ,DeptStartUp6
from django.contrib import messages

# Create your views here.
# for Adding and showing new entrys
def add_show(request):
    if request.method == 'POST':
        form = AddStudentNew(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/')

    form = AddStudentNew()

    stud = StudentNew.objects.all()
    context = {
        'header': 'Student Result',
        'form':form,
        'stu':stud
    }
    
    return render(request, 'department/add_show.html', context)

# Update/Edit table item
def update_data(request, id):
    if request.method == 'POST' :
        pi = StudentNew.objects.get(pk=id)
        form = AddStudentNew(request.POST, instance=pi)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Changes Saved !')
    else:
        pi = StudentNew.objects.get(pk=id)
        form = AddStudentNew(instance=pi)
    return render(request, 'department/update_row.html', {'form':form})

# Delete function
def delete_data(request, id):
    if request.method == 'POST' :
        pi = StudentNew.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def dept_act_2(request):
    return render(request, 'department/dept_act_2.html')


def dept_act_3(request):
    form = AddProEvent()
    if request.method == 'POST':
        form = AddProEvent(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_3')
            #return dept_act_3(request)
    else:
        form = AddProEvent()
    event = ProEvent.objects.all

    context = {
        'header': 'Departmental Activities',
        'form' : form,
        'event' : event,        
    }
    return render(request, 'department/dept_act_3.html', context)

def dept_act_4(request):

    form = AddStudPart()
    if request.method == 'POST':
        form = AddStudPart(request.POST)
        if form.is_valid:
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_4')
    event = DeptStudPart.objects.all()

    context = {
        'header': "Students Inter-Institute Participation",
        'form': form,
        'event': event,
    }

    return render(request, 'department/dept_act_4.html', context)

def dept_act_5(request):

    form = AddStudPart5()
    if request.method == 'POST':
        form = AddStudPart5(request.POST)
        if form.is_valid:
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_5')
    event = DeptStudPart5.objects.all()

    context = {
        'header': "Students Inter-Institute Participation",
        'form': form,
        'event': event,
    }

    return render(request, 'department/dept_act_5.html', context)

def dept_act_6(request):

    form = AddStartUp6()
    if request.method == 'POST':
        form = AddStartUp6(request.POST)
        if form.is_valid:
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_6')

    event = DeptStartUp6.objects.all()

    context = {
        'header': "Start Up",
        'form': form,
        'event': event,
    }

    return render(request, 'department/dept_act_6.html', context)