from django.shortcuts import render, HttpResponseRedirect
from .forms import AddStudent, AddProEvent, AddStudPart
from .models import StudentResult, DeptProEvent3, DeptStudPart5
from django.contrib import messages

# Create your views here.

#-------------------------------------------------------------------------------------
# for Adding and showing new entrys
def add_show(request):
    form = AddStudent(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/')
        form = AddStudent() 
    else:
        form = AddStudent()

    students = StudentResult.objects.all()
    context = {
        'header': 'Student Result',
        'form':form,
        'stu':students
    }
    
    return render(request, 'department/add_show.html', context)

# Update/Edit table item
def update_data(request, id):
    if request.method == 'POST' :
        pi = StudentResult.objects.get(pk=id)
        form = AddStudent(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Saved !')
    else:
        pi = StudentResult.objects.get(pk=id)
        form = AddStudent(instance=pi)
    return render(request, 'department/update_row.html', {'form':form})

# Delete function
def delete_data(request, id):
    if request.method == 'POST' :
        pi = StudentResult.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#------------------------------------------------------------------------------------
def dept_act_3(request):
    form = AddProEvent()
    if request.method == 'POST':
        form = AddProEvent(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_3')
    else:
        form = AddProEvent()
    event = DeptProEvent3.objects.all

    context = {
        'header': 'Department Events With Professional Bodies',
        'form' : form,
        'event' : event,        
    }
    return render(request, 'department/dept_act_3.html', context)

def dept_act_5(request):
    form = AddStudPart()
    if request.method == 'POST':
        form = AddStudPart(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_5')
    event = DeptStudPart5.objects.all()

    context = {
        'header': "Students Inter-Institute Participation",
        'form': form,
        'event': event,
    }

    return render(request, 'department/dept_act_5.html', context)
