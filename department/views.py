from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *
from django.views.generic import (CreateView, DetailView, UpdateView, DeleteView)
from django.forms.models import model_to_dict
from django.core import serializers
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

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
@login_required
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
@login_required
def delete_data(request, id):
    if request.method == 'POST' :
        pi = StudentResult.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#------------------------------------------------------------------------------------
#------------------------DEPARTMENTAL ACTIVITIES-------------------------------------
class DeptEvent1Create(CreateView):
    model = DeptEvent1
    form_class = AddDeptEvent1
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Events Organized by Department'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "dept_act_1"
        context['update_link'] = "dept_act_1_update"
        context['delete_link'] = "dept_act_1_delete"
        context['tab_link'] = "dept_act_tabs.html"
        return context
@method_decorator(login_required, name='dispatch')
class DeptEvent1Update(UpdateView):
    model = DeptEvent1
    form_class = AddDeptEvent1
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Events Organized by Department'
        return context
@method_decorator(login_required, name='dispatch')
class DeptEvent1Delete(DeleteView):
    model = DeptEvent1
    success_url = reverse_lazy("dept_act_1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "dept_act_1"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#------------------------------------------------------------------------------------
class DeptEvent2Create(CreateView):
    model = DeptEvent2
    form_class = AddDeptEvent2
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Events Organized by Department (For Nearby Schools)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "dept_act_2"
        context['update_link'] = "dept_act_2_update"
        context['delete_link'] = "dept_act_2_delete"
        context['tab_link'] = "dept_act_tabs.html"
        return context

class DeptEvent2Update(UpdateView):
    model = DeptEvent2
    form_class = AddDeptEvent2
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Events Organized by Department (For Nearby Schools)'
        return context

class DeptEvent2Delete(DeleteView):
    model = DeptEvent2
    success_url = reverse_lazy("dept_act_2")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "dept_act_2"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------------------
class DeptProEvent3Create(CreateView):
    model = DeptProEvent3
    form_class = AddDeptProEvent3
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Department Events With Professional Bodies'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "dept_act_3"
        context['update_link'] = "dept_act_3_update"
        context['delete_link'] = "dept_act_3_delete"
        context['tab_link'] = "dept_act_tabs.html"
        return context

class DeptProEvent3Update(UpdateView):
    model = DeptProEvent3
    form_class = AddDeptProEvent3
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Department Events With Professional Bodies'
        return context

class DeptProEvent3Delete(DeleteView):
    model = DeptProEvent3
    success_url = reverse_lazy("dept_act_3")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "dept_act_3"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------------------
class DeptFacultyDev4Create(CreateView):
    model = DeptFacultyDev4
    form_class = AddDeptFacultyDev4
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Departmental Faculty Development Programs'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "dept_act_4"
        context['update_link'] = "dept_act_4_update"
        context['delete_link'] = "dept_act_4_delete"
        context['tab_link'] = "dept_act_tabs.html"
        return context

class DeptFacultyDev4Update(UpdateView):
    model = DeptFacultyDev4
    form_class = AddDeptFacultyDev4
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Departmental Faculty Development Programs'
        return context

class DeptFacultyDev4Delete(DeleteView):
    model = DeptFacultyDev4
    success_url = reverse_lazy("dept_act_4")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "dept_act_4"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------------------
class DeptStudPart5Create(CreateView):
    model = DeptStudPart5
    form_class = AddDeptStudPart5
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Student's Inter-Institute Participation"
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "dept_act_5"
        context['update_link'] = "dept_act_5_update"
        context['delete_link'] = "dept_act_5_delete"
        context['tab_link'] = "dept_act_tabs.html"
        return context

class DeptStudPart5Update(UpdateView):
    model = DeptStudPart5
    form_class = AddDeptStudPart5
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Student's Inter-Institute Participation"
        return context

class DeptStudPart5Delete(DeleteView):
    model = DeptStudPart5
    success_url = reverse_lazy("dept_act_5")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "dept_act_5"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------------------
class DeptStartUp6Create(CreateView):
    model = DeptStartUp6
    form_class = AddDeptStartUp6
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Start-Ups'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "dept_act_6"
        context['update_link'] = "dept_act_6_update"
        context['delete_link'] = "dept_act_6_delete"
        context['tab_link'] = "dept_act_tabs.html"
        return context

class DeptStartUp6Update(UpdateView):
    model = DeptStartUp6
    form_class = AddDeptStartUp6
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Start-Ups'
        return context

class DeptStartUp6Delete(DeleteView):
    model = DeptStartUp6
    success_url = reverse_lazy("dept_act_6")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "dept_act_6"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------------------
#-------------------------------FACULTY ACHIEVEMENTS----------------------------------

class FacAchieveCreate(CreateView):
    model = FacAchieve
    form_class = AddFacAchieve
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Achievement List'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_achieve"
        context['update_link'] = "fac_achieve_update"
        context['delete_link'] = "fac_achieve_delete"
        context['tab_link'] = "fac_tabs.html"
        return context

class FacAchieveUpdate(UpdateView):
    model = FacAchieve
    form_class = AddFacAchieve
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Achievement List'
        return context

class FacAchieveDelete(DeleteView):
    model = FacAchieve
    success_url = reverse_lazy("fac_achieve")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_achieve"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------------------
class FacBookCreate(CreateView):
    model = FacBook
    form_class = AddFacBook
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'BOOKS AND MONOGRAPHS PUBLISHED'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_achieve"
        context['update_link'] = "fac_book_update"
        context['delete_link'] = "fac_book_delete"
        context['tab_link'] = "fac_tabs.html"
        return context

class FacBookUpdate(UpdateView):
    model = FacBook
    form_class = AddFacBook
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'BOOKS AND MONOGRAPHS PUBLISHED'
        return context

class FacBookDelete(DeleteView):
    model = FacBook
    success_url = reverse_lazy("fac_book")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_book"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------------------
#-------------------------------CURRICULUM INPUT--------------------------------------
class CurGuestLect1Create(CreateView):
    model = CurGuestLect1
    form_class = AddCurGuestLect1
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Guest Lectures (General Topics)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "cur_input_1"
        context['update_link'] = "cur_input_1_update"
        context['delete_link'] = "cur_input_1_delete"
        context['tab_link'] = "cur_input_tabs.html"
        return context

class CurGuestLect1Update(UpdateView):
    model = CurGuestLect1
    form_class = AddCurGuestLect1
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Guest Lectures (General Topics)'
        return context

class CurGuestLect1Delete(DeleteView):
    model = CurGuestLect1
    success_url = reverse_lazy("cur_input_1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "cur_input_1"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------
class CurExptLect2Create(CreateView):
    model = CurExptLect2
    form_class = AddCurExptLect2
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "cur_input_2"
        context['update_link'] = "cur_input_2_update"
        context['delete_link'] = "cur_input_2_delete"
        context['tab_link'] = "cur_input_tabs.html"
        return context

class CurExptLect2Update(UpdateView):
    model = CurExptLect2
    form_class = AddCurExptLect2
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        return context

class CurExptLect2Delete(DeleteView):
    model = CurExptLect2
    success_url = reverse_lazy("cur_input_2")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "cur_input_2"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#-------------------------------------------------------------------------
class CurStudTrain3Create(CreateView):
    model = CurStudTrain3
    form_class = AddCurStudTrain3
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "cur_input_3"
        context['update_link'] = "cur_input_3_update"
        context['delete_link'] = "cur_input_3_delete"
        context['tab_link'] = "cur_input_tabs.html"
        return context

class CurStudTrain3Update(UpdateView):
    model = CurStudTrain3
    form_class = AddCurStudTrain3
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        return context

class CurStudTrain3Delete(DeleteView):
    model = CurStudTrain3
    success_url = reverse_lazy("cur_input_3")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "cur_input_3"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------
class CurStudVisit4Create(CreateView):
    model = CurStudVisit4
    form_class = AddCurStudVisit4
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "cur_input_4"
        context['update_link'] = "cur_input_4_update"
        context['delete_link'] = "cur_input_4_delete"
        context['tab_link'] = "cur_input_tabs.html"
        return context

class CurStudVisit4Update(UpdateView):
    model = CurStudVisit4
    form_class = AddCurStudVisit4
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        return context

class CurStudVisit4Delete(DeleteView):
    model = CurStudVisit4
    success_url = reverse_lazy("cur_input_4")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "cur_input_4"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context
#--------------------------------------------------------------------------

# def cur_input_5(request):

#     form = AddCurStudSponsor5()
#     if request.method == "POST":
#         form = AddCurStudSponsor5(request.POST)
#         form.save()
#         messages.success(request, 'Added successfully')
#         return HttpResponseRedirect('cur_input_5')

#     items = CurStudSponsor5.objects.all()
    
#     context = {
#         'header': 'Students Sponsored Projects',
#         'form': form,
#         'items': items,
#         'nbar': 'cur_input_5',
#     }

#     return render(request, 'cur_input_5.html', context)

class CurStudSponsor5Create(CreateView):
    model = CurStudSponsor5
    form_class = AddCurStudSponsor5
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "cur_input_5"
        context['update_link'] = "cur_input_5_update"
        context['delete_link'] = "cur_input_5_delete"
        context['tab_link'] = "cur_input_tabs.html"
        return context

class CurStudSponsor5Update(UpdateView):
    model = CurStudSponsor5
    form_class = AddCurStudSponsor5
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Expert Lectures'
        return context

class CurStudSponsor5Delete(DeleteView):
    model = CurStudSponsor5
    success_url = reverse_lazy("cur_input_5")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "cur_input_5"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context
    
#---------------Industry-Institute Interaction-----------------------------------------------------
#--------------------------------------------------------------------------------------------------
# Class Based View **note layout**
# 1]Industrial Visit  of Faculty (Visits accompanied with students should be excluded)
class IndInst1Create(CreateView):
    model = IndFacvisit1
    form_class = IndFacVisit1Form
    template_name = 'create_form.html'
    context_object_name = 'ind_inst_1_instance'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Industrial Visit  of Faculty (Visits accompanied with students should be excluded)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_1_tab"
        context['update_link'] = "ind_inst_1_update"
        context['delete_link'] = "ind_inst_1_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst1Update(UpdateView):
    model = IndFacvisit1
    form_class = IndFacVisit1Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Industrial Visit  of Faculty (Visits accompanied with students should be excluded)'
        return context

class IndInst1Delete(DeleteView):
    model = IndFacvisit1
    success_url = reverse_lazy("ind_inst_1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_1"
        return context
#-------------------------------------------------------------------------------------------------
#2] Training of Faculty by Industry
class IndInst2Create(CreateView):
    model = IndInst2
    form_class = IndInst2Form
    template_name = 'create_form.html'
    # context_object_name = 'ind_inst_2_instance'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Training of Faculty by Industry'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_2_tab"
        context['update_link'] = "ind_inst_2_update"
        context['delete_link'] = "ind_inst_2_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst2Update(UpdateView):
    model = IndInst2
    form_class = IndInst2Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Training of Faculty by Industry'

        return context

class IndInst2Delete(DeleteView):
    model = IndInst2
    success_url = reverse_lazy("ind_inst_2")
    template_name = "form_delete.html"
    context_object_name = "model_instance"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_2"
        return context

#-------------------------------------------------------------------------------------------------
#3] Faculty Providing training to industry
class IndInst3Create(CreateView):
    model = IndInst3
    form_class = IndInst3Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Faculty Providing training to Industry'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_3_tab"
        context['update_link'] = "ind_inst_3_update"
        context['delete_link'] = "ind_inst_3_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst3Update(UpdateView):
    model = IndInst3
    form_class = IndInst3Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Faculty Providing training to Industry'
        return context

class IndInst3Delete(DeleteView):
    model = IndInst3
    success_url = reverse_lazy("ind_inst_3")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_3"
        return context

#-------------------------------------------------------------------------------------------------
#4] Faculty on board of Industry
class IndInst4Create(CreateView):
    model = IndInst4Model
    form_class = IndInst4FormNew
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Faculty on board of Industry'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_4_tab"
        context['update_link'] = "ind_inst_4_update"
        context['delete_link'] = "ind_inst_4_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst4Update(UpdateView):
    model = IndInst4Model
    form_class = IndInst4FormNew
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Faculty on board of Industry'
        return context

class IndInst4Delete(DeleteView):
    model = IndInst4Model
    success_url = reverse_lazy("ind_inst_4")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_4"
        return context

#-------------------------------------------------------------------------------------------------
#5] Faculty on board of Industry
class IndInst5Create(CreateView):
    model = IndInst5
    form_class = IndInst5Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Industrial people on various Boards/Committee of Institute or Department '
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_5_tab"
        context['update_link'] = "ind_inst_5_update"
        context['delete_link'] = "ind_inst_5_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst5Update(UpdateView):
    model = IndInst5
    form_class = IndInst5Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Industrial people on various Boards/Committee of Institute or Department '
        return context

class IndInst5Delete(DeleteView):
    model = IndInst5
    success_url = reverse_lazy("ind_inst_5")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_5"
        return context

#-------------------------------------------------------------------------------------------------
#6] Faculty patents leading to industry products
class IndInst6Create(CreateView):
    model = IndInst6
    form_class = IndInst6Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Faculty patents leading to industry products'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_6_tab"
        context['update_link'] = "ind_inst_6_update"
        context['delete_link'] = "ind_inst_6_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst6Update(UpdateView):
    model = IndInst6
    form_class = IndInst6Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Faculty patents leading to industry products'
        return context

class IndInst6Delete(DeleteView):
    model = IndInst6
    success_url = reverse_lazy("ind_inst_6")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_6"
        return context

#-------------------------------------------------------------------------------------------------
#7] Sponsored Projects (Faculty only)
class IndInst7Create(CreateView):
    model = IndInst7
    form_class = IndInst7Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Sponsored Projects (Faculty only)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_7_tab"
        context['update_link'] = "ind_inst_7_update"
        context['delete_link'] = "ind_inst_7_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst7Update(UpdateView):
    model = IndInst7
    form_class = IndInst7Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Sponsored Projects (Faculty only)'
        return context

class IndInst7Delete(DeleteView):
    model = IndInst7
    success_url = reverse_lazy("ind_inst_7")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_7"
        return context

#-------------------------------------------------------------------------------------------------
#8] Consultancy Projects/Advisory Services
class IndInst8Create(CreateView):
    model = IndInst8
    form_class = IndInst8Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Consultancy Projects/Advisory Services'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_8_tab"
        context['update_link'] = "ind_inst_8_update"
        context['delete_link'] = "ind_inst_8_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst8Update(UpdateView):
    model = IndInst8
    form_class = IndInst8Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Consultancy Projects/Advisory Services'
        return context

class IndInst8Delete(DeleteView):
    model = IndInst8
    success_url = reverse_lazy("ind_inst_8")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_8"
        return context

#-------------------------------------------------------------------------------------------------
# 9] MOU Information
class IndInst9Create(CreateView):
    model = IndInst9
    form_class = IndInst9Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'MOU Information'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "ind_inst_9_tab"
        context['update_link'] = "ind_inst_9_update"
        context['delete_link'] = "ind_inst_9_delete"
        context['tab_link'] = "ind_inst_tabs.html"
        return context

class IndInst9Update(UpdateView):
    model = IndInst9
    form_class = IndInst9Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'MOU Information'
        return context

class IndInst9Delete(DeleteView):
    model = IndInst9
    success_url = reverse_lazy("ind_inst_9")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "ind_inst_9"
        return context
