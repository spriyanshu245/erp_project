from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import FacAchieve, StudentResult, DeptEvent1, DeptEvent2, DeptProEvent3, DeptFacultyDev4, DeptStudPart5, DeptStartUp6
from django.contrib import messages

# Create your views here.


#-------------------------------------------------------------------------------------
# for Adding and showing new entrys
def add_show(request):
    if request.method == 'POST':
        form = AddStudentResult(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/')
    else:
        form = AddStudentResult()

    students = StudentResult.objects.all()
    context = {
        'header': 'Student Result',
        'form':form,
        'stu':students
    }
    
    return render(request, 'add_show.html', context)

# Update/Edit table item
def update_data(request, id):
    if request.method == 'POST' :
        pi = StudentResult.objects.get(pk=id)
        form = AddStudentResult(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Saved !')
    else:
        pi = StudentResult.objects.get(pk=id)
        form = AddStudentResult(instance=pi)
    return render(request, 'update_row.html', {'form':form})

# Delete function
def delete_data(request, id):
    if request.method == 'POST' :
        pi = StudentResult.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#------------------------------------------------------------------------------------
def dept_act_1(request):
    form = AddDeptEvent1()
    if request.method == 'POST':
        form = AddDeptEvent1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully")
            return HttpResponseRedirect('/department/dept_act_1')

    event = DeptEvent1.objects.all()

    context = {
        'header': 'Events Organized by Department ',
        'form' : form,
        'event' : event,        
    }

    return render(request, 'dept_act_1.html', context)

#  # Delete View 
# class dept_act_1DeleteView(DeleteView):  
#     model = DeptEvent1 
      
#     # specify success url 
#     # to redirect after successfully 
#     # deleting object 
#     success_url ='/department/dept_act_1'

#------------------------------------------------------------------------------------
def dept_act_2(request):
    form = AddDeptEvent2()
    if request.method == 'POST':
        form = AddDeptEvent2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully")
            return HttpResponseRedirect('/department/dept_act_2')

    event = DeptEvent2.objects.all()

    context = {
        'header': 'Events Organized by Department (For Nearby Schools)',
        'form' : form,
        'event' : event,        
    }

    return render(request, 'dept_act_2.html', context)

#-------------------------------------------------------------------------------------
def dept_act_3(request):
    form = AddDeptProEvent3()
    if request.method == 'POST':
        form = AddDeptProEvent3(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_3')
    else:
        form = AddDeptProEvent3()

    event = DeptProEvent3.objects.all

    context = {
        'header': 'Department Events With Professional Bodies',
        'form' : form,
        'event' : event,        
    }
    return render(request, 'dept_act_3.html', context)



#-------------------------------------------------------------------------------------
def dept_act_4(request):
    form = AddDeptFacultyDev4()
    if request.method == 'POST':
        form = AddDeptFacultyDev4(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_4')

    event = DeptFacultyDev4.objects.all()

    context = {
        'header': "Departmental Faculty Development Programs",
        'form': form,
        'event': event,
    }

    return render(request, 'dept_act_4.html', context)

#-------------------------------------------------------------------------------------
def dept_act_5(request):
    form = AddDeptStudPart5()
    if request.method == 'POST':
        form = AddDeptStudPart5(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_5')
    event = DeptStudPart5.objects.all()

    context = {
        'header': "Student's Inter-Institute Participation",
        'form': form,
        'event': event,
    }

    return render(request, 'dept_act_5.html', context)

#-------------------------------------------------------------------------------------
def dept_act_6(request):

    form = AddDeptStartUp6()
    if request.method == 'POST':
        form = AddDeptStartUp6(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/dept_act_6')

    event = DeptStartUp6.objects.all()

    context = {
        'header': "Start-Up",
        'form': form,
        'event': event,
    }

    return render(request, 'dept_act_6.html', context)

    #-------------------------------------------------------------------------------------

def fac_achieve(request):

    # form = AddFacAchievements()
    # if request.method == "POST":
    #     form = AddFacAchievements(request.POST)

    context = {
        'header': "Achievement List",
    }

    return render(request, 'fac_achieve.html', context)
    
