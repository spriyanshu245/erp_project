from django.shortcuts import render, HttpResponseRedirect
from .forms import AddStudentNew, AddProEvent, AddStudPart ,AddFDOP_Dept , AddStartUP
from .models import StudentNew, ProEvent, DeptStudPart , FacultyDevProOrg_Dep ,StartUp
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
            
            # cd = form.cleaned_data
            # nm = cd['name']
            # dp = cd['departments']
            # em = cd['employer']
            # dt = cd['date']
            # pk = cd['package']
            # rf = cd['ref_no']
            # ya = cd['year_admission']
            # yd = cd['year_down']
            #model class object created (reg)
            # reg = Student(name=nm, departments=dp, employer=em,date=dt, package=pk, ref_no=rf,year_admission=ya,year_down=yd)
   
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

    form = AddFDOP_Dept()
    if request.method == 'POST':
        form = AddFDOP_Dept(request.POST)
        if form.is_valid:
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_5')
    event = FacultyDevProOrg_Dep.objects.all()

    context = {
        'header': "Students Inter-Institute Participation",
        'form': form,
        'event': event,
    }

    return render(request, 'department/dept_act_5.html', context)

def dept_act_6(request):

    form = AddStartUP()
    if request.method == 'POST':
        form = AddStartUP(request.POST)
        if form.is_valid:
            form.save(commit=True)
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_6')
    event = StartUp.objects.all()

    context = {
        'header': "Students Inter-Institute Participation",
        'form': form,
        'event': event,
    }

    return render(request, 'department/dept_act_6.html', context)
