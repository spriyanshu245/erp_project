from django.shortcuts import render, HttpResponseRedirect
from .forms import AddStudent, AddProEvent
from .models import Student, ProEvent
from django.contrib import messages

# Create your views here.
# for Adding and showing new entrys
def add_show(request):
    form = AddStudent(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            nm = cd['name']
            dp = cd['departments']
            em = cd['employer']
            dt = cd['date']
            pk = cd['package']
            rf = cd['ref_no']
            #model class object created (reg)
            reg = Student(name=nm, departments=dp, employer=em,date=dt, package=pk, ref_no=rf)
            reg.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/')
        form = AddStudent() 
    else:
        form = AddStudent()

    stud = Student.objects.all()
    context = {
        'header': 'Student Result',
        'form':form,
        'stu':stud
    }
    
    return render(request, 'department/add_show.html', context)

# Update/Edit table item
def update_data(request, id):
    if request.method == 'POST' :
        pi = Student.objects.get(pk=id)
        form = AddStudent(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Saved !')
    else:
        pi = Student.objects.get(pk=id)
        form = AddStudent(instance=pi)
    return render(request, 'department/update_row.html', {'form':form})

# Delete function
def delete_data(request, id):
    if request.method == 'POST' :
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def dept_act_3(request):
    form = AddProEvent()
    if request.method == 'POST':
        form = AddProEvent(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('department/dept_act_3.html')
            #return dept_act_3(request)
    else:
        form = AddProEvent()
    event = ProEvent.objects.all()

    context = {
        'header': 'Departmental Activities',
        'form' : form
        #'event' : event
    }
    return render(request, 'department/dept_act_3.html', context)
