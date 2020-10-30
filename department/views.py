from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic import (CreateView, DetailView, UpdateView, DeleteView)
from django.forms.models import model_to_dict
from django.core import serializers

# Custom templates

# Create your views here.

#-------------------------------STUDENT RESULTS-----------------------------------------
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
#------------------------DEPARTMENTAL ACTIVITIES-------------------------------------
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
        'nbar': 'dept_act_1',     
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
        'nbar': 'dept_act_2',     
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

    event = DeptProEvent3.objects.all()

    context = {
        'header': 'Department Events With Professional Bodies',
        'form' : form,
        'event' : event,  
        'nbar': 'dept_act_3'      
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
        'nbar': 'dept_act_4'
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
        'nbar': 'dept_act_5'
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
        'nbar': 'dept_act_6'
    }

    return render(request, 'dept_act_6.html', context)

#-------------------------------------------------------------------------------------
#-------------------------------FACULTY ACHIEVEMENTS----------------------------------

def fac_achieve(request):
    form = AddFacAchieve()
    if request.method == "POST":
        form = AddFacAchieve(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/department/fac_achieve')
    else:
        form = AddFacAchieve()
             
    items = FacAchieve.objects.all()

    context = {
        'header': "ACHIEVEMENT LIST",
        'items': items,
        'form': form
    }

    return render(request, 'fac_achieve.html', context)

#-------------------------------------------------------------------------------------
def fac_book(request):
    form = AddFacBook()
    if request.method == 'POST':
        form = AddFacBook(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully")
            return HttpResponseRedirect('/department/fac_book')

    items = FacBook.objects.all()

    context = {
        'header': 'BOOKS AND MONOGRAPHS PUBLISHED',
        'items': items,
        'form': form       
    }

    return render(request, 'fac_book.html', context)

#-------------------------------------------------------------------------------------
#-------------------------------CURRICULUM INPUT--------------------------------------
def cur_input_1(request):
    form = AddCurGuestLect1()
    if request.method == 'POST':
        form = AddCurGuestLect1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully")
            return HttpResponseRedirect('curr_input_1')

    items = CurGuestLect1.objects.all()

    context = {
        'header': 'Guest Lectures (General Topics)',
        'form': form,
        'items': items,
        'nbar': 'cur_input_1',        
    }

    return render(request, 'cur_input_1.html', context)

#-------------------------------------------------------------------------
def cur_input_2(request):
    form = AddCurExptLect2()
    if request.method == 'POST':
        form = AddCurExptLect2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added successfully")
            return HttpResponseRedirect('cur_input_2')

    items = CurExptLect2.objects.all()

    context = {
        'header': 'Expert Lectures',
        'form': form,
        'items': items,
        'nbar': 'cur_input_2',        
    }

    return render(request, 'cur_input_2.html', context)

#-------------------------------------------------------------------------
def cur_input_3(request):
    form = AddCurStudTrain3()
    if request.method == "POST":
        form = AddCurStudTrain3(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('cur_input_3')

    items = CurStudTrain3.objects.all()

    context = {
        'header': 'Student Internship/Industrial Training',
        'form': form,
        'items': items,
        'nbar': 'cur_input_3',
    }

    return render(request, 'cur_input_3.html', context)

#--------------------------------------------------------------------------
def cur_input_4(request):

    form = AddCurStudVisit4()
    if request.method == "POST":
        form = AddCurStudVisit4(request.POST)
        form.save()
        messages.success(request, 'Added successfully')
        return HttpResponseRedirect('cur_input_4')

    items = CurStudVisit4.objects.all()

    context = {
        'header': 'Student Industrial Visit',
        'form': form,
        'items': items,
        'nbar': 'cur_input_4',
    }

    return render(request, 'cur_input_4.html', context)

#--------------------------------------------------------------------------
def cur_input_5(request):

    form = AddCurStudSponsor5()
    if request.method == "POST":
        form = AddCurStudSponsor5(request.POST)
        form.save()
        messages.success(request, 'Added successfully')
        return HttpResponseRedirect('cur_input_5')

    items = CurStudSponsor5.objects.all()
    
    context = {
        'header': 'Students Sponsored Projects',
        'form': form,
        'items': items,
        'nbar': 'cur_input_5',
    }

    return render(request, 'cur_input_5.html', context)
    
#---------------Industry-Institute Interaction-----------------------------

# Class Based View **note layout**
# 1]Industrial Visit  of Faculty (Visits accompanied with students should be excluded)
class IndInst1Create(CreateView):
    model = IndFacvisit1
    form_class = IndFacVisit1Form
    template_name = 'ind_inst_1_form.html'
    context_object_name = 'contextobj'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        context['header'] = 'Industrial Visit  of Faculty (Visits accompanied with students should be excluded)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

class IndInst1Update(UpdateView):
    model = IndFacvisit1
    form_class = IndFacVisit1Form
    template_name = "ind_inst_1_update.html"