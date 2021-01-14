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

#----------------------------------STUDENT ACADEMIC PERFORMANCE--------------------------------====

class StudentResultCreate(CreateView):
    model = StudentResult
    form_class = AddStudentResult
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Students Result in various examinations'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "stud_result"
        context['update_link'] = "stud_result_update"
        context['delete_link'] = "stud_result_delete"
        context['tab_link'] = "stud_result_tabs.html"
        context['count'] = self.model.objects.all().count()
        return context
        
@method_decorator(login_required, name='dispatch')
class StudentResultUpdate(UpdateView):
    model = StudentResult
    form_class = AddStudentResult
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Students Result in various examinations'
        return context

@method_decorator(login_required, name='dispatch')
class StudentResultDelete(DeleteView):
    model = StudentResult
    success_url = reverse_lazy("stud_result")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "stud_result"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#------------------------------------DEPARTMENTAL ACTIVITIES---------------------------------------

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

#--------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------
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

        
#--------------------------------------------------------------------------------------------------
#--------------------------------------FACULTY CONTRIBUTIONS---------------------------------------
# count class of all faculty contribution tables

#1] Research projects in the specified period
class ResProject1Create(CreateView):
    model = ResProject1
    form_class = AddResProject1
    template_name = 'create_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research projects in the specified period'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_1"
        context['update_link'] = "fac_contri_1_update"
        context['delete_link'] = "fac_contri_1_delete"
        context['tab_link'] = "fac_contri_tabs.html"

        titles = ['Research projects in the specified period',
        'Funds received for research for projects',
        'Research papers published in International journals',
        'Research papers published in National journals',
        'Paper presented in International Conferences',
        'Paper presented in National Conferences',
        'Research papers authored with industrial persons',
        'Events for faculty members (FDP/Webinar/Seminar/STTP/Workshops/Others)',
        'Participation in Professional Practices (Curriculum Revision/Syllabus Development)',
        'List of Faculty Patents/IPR']
        counts = [self.model.objects.all().count(),
        ResFunds2Create.model.objects.all().count(),
        ResInternational3Create.model.objects.all().count(),
        ResNational4Create.model.objects.all().count(),
        ConfInternational5Create.model.objects.all().count(),
        ConfNational6Create.model.objects.all().count(),
        ResIndustrial7Create.model.objects.all().count(),
        FacEvents8Create.model.objects.all().count(),
        ProfessionalPrac9Create.model.objects.all().count(),
        FacPatents10Create.model.objects.all().count()]
        context['title'] = titles
        context['count'] = counts
        return context


class ResProject1Update(UpdateView):
    model = ResProject1
    form_class = AddResProject1
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research projects in the specified period'
        return context

class ResProject1Delete(DeleteView):
    model = ResProject1
    success_url = reverse_lazy("fac_contri_1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_1"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#2] Funds received for research for projects
class ResFunds2Create(CreateView):
    model = ResFunds2
    form_class = AddResFunds2
    template_name = 'create_form.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Funds received for research for projects'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_2"
        context['update_link'] = "fac_contri_2_update"
        context['delete_link'] = "fac_contri_2_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        # context['count'] = self.model.objects.all().count()
        return context

class ResFunds2Update(UpdateView):
    model = ResFunds2
    form_class = AddResFunds2
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Funds received for research for projects'
        return context

class ResFunds2Delete(DeleteView):
    model = ResFunds2
    success_url = reverse_lazy("fac_contri_2")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_2"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#3] Research papers published in International journals in the specified period
class ResInternational3Create(CreateView):
    model = ResInternational3
    form_class = AddResInternational3
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research papers published in International journals'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_3"
        context['update_link'] = "fac_contri_3_update"
        context['delete_link'] = "fac_contri_3_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class ResInternational3Update(UpdateView):
    model = ResInternational3
    form_class = AddResInternational3
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research papers published in International journals'
        return context

class ResInternational3Delete(DeleteView):
    model = ResInternational3
    success_url = reverse_lazy("fac_contri_3")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_3"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#4] Research papers published in national journals in the specified period
class ResNational4Create(CreateView):
    model = ResNational4
    form_class = AddResNational4
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research papers published in National journals'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_4"
        context['update_link'] = "fac_contri_4_update"
        context['delete_link'] = "fac_contri_4_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class ResNational4Update(UpdateView):
    model = ResNational4
    form_class = AddResNational4
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research papers published in National journals'
        return context

class ResNational4Delete(DeleteView):
    model = ResNational4
    success_url = reverse_lazy("fac_contri_4")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_4"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#5] Paper presented in International Conferences in the specified period
class ConfInternational5Create(CreateView):
    model = ConfInternational5
    form_class = AddConfInternational5
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Paper presented in International Conferences'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_5"
        context['update_link'] = "fac_contri_5_update"
        context['delete_link'] = "fac_contri_5_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class ConfInternational5Update(UpdateView):
    model = ConfInternational5
    form_class = AddConfInternational5
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Paper presented in International Conferences'
        return context

class ConfInternational5Delete(DeleteView):
    model = ConfInternational5
    success_url = reverse_lazy("fac_contri_5")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_5"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#6] Paper presented in National Conferences in the specified period
class ConfNational6Create(CreateView):
    model = ConfNational6
    form_class = AddConfNational6
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Paper presented in National Conferences'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_6"
        context['update_link'] = "fac_contri_6_update"
        context['delete_link'] = "fac_contri_6_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class ConfNational6Update(UpdateView):
    model = ConfNational6
    form_class = AddConfNational6
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Paper presented in National Conferences'
        return context

class ConfNational6Delete(DeleteView):
    model = ConfNational6
    success_url = reverse_lazy("fac_contri_6")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_6"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#7] Research papers authored with industrial persons
class ResIndustrial7Create(CreateView):
    model = ResIndustrial7
    form_class = AddResIndustrial7
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research papers authored with industrial persons'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_7"
        context['update_link'] = "fac_contri_7_update"
        context['delete_link'] = "fac_contri_7_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class ResIndustrial7Update(UpdateView):
    model = ResIndustrial7
    form_class = AddResIndustrial7
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Research papers authored with industrial persons'
        return context

class ResIndustrial7Delete(DeleteView):
    model = ResIndustrial7
    success_url = reverse_lazy("fac_contri_7")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_7"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#8] Events for faculty members (FDP/Webinar/Seminar/STTP/Workshops/Others)
class FacEvents8Create(CreateView):
    model = FacEvents8
    form_class = AddFacEvents8
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Events for faculty members (FDP/Webinar/Seminar/STTP/Workshops/Others)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_8"
        context['update_link'] = "fac_contri_8_update"
        context['delete_link'] = "fac_contri_8_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class FacEvents8Update(UpdateView):
    model = FacEvents8
    form_class = AddFacEvents8
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Events for faculty members (FDP/Webinar/Seminar/STTP/Workshops/Others)'
        return context

class FacEvents8Delete(DeleteView):
    model = FacEvents8
    success_url = reverse_lazy("fac_contri_8")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_8"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#9] Participation in Professional Practices (Curriculum Revision/Syllabus Development/Others)
class ProfessionalPrac9Create(CreateView):
    model = ProfessionalPrac9
    form_class = AddProfessionalPrac9
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Participation in Professional Practices (Curriculum Revision/Syllabus Development)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_9"
        context['update_link'] = "fac_contri_9_update"
        context['delete_link'] = "fac_contri_9_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class ProfessionalPrac9Update(UpdateView):
    model = ProfessionalPrac9
    form_class = AddProfessionalPrac9
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Participation in Professional Practices (Curriculum Revision/Syllabus Development)'
        return context

class ProfessionalPrac9Delete(DeleteView):
    model = ProfessionalPrac9
    success_url = reverse_lazy("fac_contri_9")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_9"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context

#--------------------------------------------------------------------------------------------------
#10] List of Faculty Patents/IPR
class FacPatents10Create(CreateView):
    model = FacPatents10
    form_class = AddFacPatents10
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of Faculty Patents/IPR'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_contri_10"
        context['update_link'] = "fac_contri_10_update"
        context['delete_link'] = "fac_contri_10_delete"
        context['tab_link'] = "fac_contri_tabs.html"
        return context

class FacPatents10Update(UpdateView):
    model = FacPatents10
    form_class = AddFacPatents10
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of Faculty Patents/IPR'
        return context

class FacPatents10Delete(DeleteView):
    model = FacPatents10
    success_url = reverse_lazy("fac_contri_10")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "fac_contri_10"
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        return context


#--------------------------------------------------------------------------------------------------
# #4] Research papers published in national journals in the specified period
# class ResNational4Create(CreateView):
#     model = ResNational4
#     form_class = AddResNational4
#     template_name = 'create_form.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['header'] = 'Research papers published in National journals'
#         context['events'] = self.model.objects.all()
#         context['data'] = serializers.serialize( "python", self.model.objects.all() )
#         context['nbar'] = "fac_contri_4"
#         context['update_link'] = "fac_contri_4_update"
#         context['delete_link'] = "fac_contri_4_delete"
#         context['tab_link'] = "fac_contri_tabs.html"
#         return context

# class ResNational4Update(UpdateView):
#     model = ResNational4
#     form_class = AddResNational4
#     template_name = "form_update.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['header'] = 'Research papers published in National journals'
#         return context

# class ResNational4Delete(DeleteView):
#     model = ResNational4
#     success_url = reverse_lazy("fac_contri_4")
#     template_name = "form_delete.html"
#     context_object_name = "model_instance"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cancel_link'] = "fac_contri_4"
#         context['data'] = serializers.serialize( "python", self.model.objects.all() )
#         return context


#--------------------------------------------------------------------------------------------------
#-------------------------------FACULTY ACHIEVEMENTS-----------------------------------------------

# 1]Achievement List
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
# 2]BOOKS & MONOGRAPHS PUBLISHED
class FacBookCreate(CreateView):
    model = FacBook
    form_class = AddFacBook
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Books & Monographs Published'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "fac_achieve"
        context['update_link'] = "fac_book_update"
        context['delete_link'] = "fac_book_delete"
        context['tab_link'] = "fac_tabs.html"
        titles = ['Number of books/chapters/Manuals/Monographs spublished',]
        counts = [self.model.objects.all().count(),]
        context['title'] = titles
        context['count'] = counts
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

#--------------------------------------------------------------------------------------------------
#-------------------------------INDUSTRY- INSTITUTE INTERACTION------------------------------------

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
    model = IndInst4
    form_class = IndInst4Form
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
    model = IndInst4
    form_class = IndInst4Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Faculty on board of Industry'
        return context

class IndInst4Delete(DeleteView):
    model = IndInst4
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

#-------------------------------------------------------------------------------------
#-------------------------------CURRICULUM INPUT--------------------------------------

# 1]Guest Lectures (General Topics)
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

#--------------------------------------------------------------------------------------------------
# 2]Expert Lectures
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

#--------------------------------------------------------------------------------------------------
# 3] Student Internship/Industrial Training 
class CurStudTrain3Create(CreateView):
    model = CurStudTrain3
    form_class = AddCurStudTrain3
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Student Internship/Industrial Training'
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

#--------------------------------------------------------------------------------------------------
# 4]Student Industrial Visit 
class CurStudVisit4Create(CreateView):
    model = CurStudVisit4
    form_class = AddCurStudVisit4
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Student Industrial Visit'
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

#--------------------------------------------------------------------------------------------------
# 5]Students Sponsored Projects
class CurStudSponsor5Create(CreateView):
    model = CurStudSponsor5
    form_class = AddCurStudSponsor5
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Students Sponsored Projects'
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
    
#------------------------------------------------------------------------------------------------------
#--------------------------------STUDENT / FACULTY SUPPORT SYSTEM--------------------------------------

#1]Mentoring System to help students at individual level
class StudFac1Create(CreateView):
    model = StudFac1
    form_class = StudFac1Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Mentoring System to help students at individual level'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "tab_1"
        context['update_link'] = "stud_fac_1_update"
        context['delete_link'] = "stud_fac_1_delete"
        context['tab_link'] = "stud_fac_tabs.html"
        return context

class StudFac1Update(UpdateView):
    model = StudFac1
    form_class = StudFac1Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Mentoring System to help students at individual level'
        return context

class StudFac1Delete(DeleteView):
    model = StudFac1
    success_url = reverse_lazy("stud_fac_1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "stud_fac_1"
        return context

#-------------------------------------------------------------------------------------------------
#2]Self Learning facilities for students
class StudFac2Create(CreateView):
    model = StudFac2
    form_class = StudFac2Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Self Learning facilities for students'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "tab_2"
        context['update_link'] = "stud_fac_2_update"
        context['delete_link'] = "stud_fac_2_delete"
        context['tab_link'] = "stud_fac_tabs.html"
        return context

class StudFac2Update(UpdateView):
    model = StudFac2
    form_class = StudFac2Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Self Learning facilities for students'
        return context

class StudFac2Delete(DeleteView):
    model = StudFac2
    success_url = reverse_lazy("stud_fac_2")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "stud_fac_2"
        return context

#-------------------------------------------------------------------------------------------------
#3]Achievement of Students in Competitive Exam
class StudFac3Create(CreateView):
    model = StudFac3
    form_class = StudFac3Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Achievement of Students in Competitive Exam '
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "tab_3"
        context['update_link'] = "stud_fac_3_update"
        context['delete_link'] = "stud_fac_3_delete"
        context['tab_link'] = "stud_fac_tabs.html"
        return context

class StudFac3Update(UpdateView):
    model = StudFac3
    form_class = StudFac1Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Achievement of Students in Competitive Exam '
        return context

class StudFac3Delete(DeleteView):
    model = StudFac3
    success_url = reverse_lazy("stud_fac_3")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "stud_fac_3"
        return context

#-------------------------------------------------------------------------------------------------
#4]Capability Enhancement and Development Activities
class StudFac4Create(CreateView):
    model = StudFac4
    form_class = StudFac4Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Capability Enhancement and Development Activities'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "tab_4"
        context['update_link'] = "stud_fac_4_update"
        context['delete_link'] = "stud_fac_4_delete"
        context['tab_link'] = "stud_fac_tabs.html"
        return context

class StudFac4Update(UpdateView):
    model = StudFac4
    form_class = StudFac4Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Capability Enhancement and Development Activities'
        return context

class StudFac4Delete(DeleteView):
    model = StudFac4
    success_url = reverse_lazy("stud_fac_4")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "stud_fac_4"
        return context

#-------------------------------------------------------------------------------------------------
#5]Number of professional development / administrative training  programmes organized
class StudFac5Create(CreateView):
    model = StudFac5
    form_class = StudFac5Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Number of professional development / administrative training  programmes organized'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "tab_5"
        context['update_link'] = "stud_fac_5_update"
        context['delete_link'] = "stud_fac_5_delete"
        context['tab_link'] = "stud_fac_tabs.html"
        return context

class StudFac5Update(UpdateView):
    model = StudFac5
    form_class = StudFac5Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Number of professional development / administrative training  programmes organized'
        return context

class StudFac5Delete(DeleteView):
    model = StudFac5
    success_url = reverse_lazy("stud_fac_5")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "stud_fac_5"
        return context

#-------------------------------------------------------------------------------------------------
#--------------------------------EXTRA CURRICULAR ACTIVITIES--------------------------------------

#1] Sports (This information to be provided by Physical/Sports Director)
class ExtraCurr1Create(CreateView):
    model = ExtraCurr1
    form_class = ExtraCurr1Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Sports (This information to be provided by Physical/Sports Director)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "tab_1"
        context['update_link'] = "extra_curr_1_update"
        context['delete_link'] = "extra_curr_1_delete"
        context['tab_link'] = "extra_curr_tabs.html"
        return context

class ExtraCurr1Update(UpdateView):
    model = ExtraCurr1
    form_class = ExtraCurr1Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Sports (This information to be provided by Physical/Sports Director)'
        return context

class ExtraCurr1Delete(DeleteView):
    model = ExtraCurr1
    success_url = reverse_lazy("extra_curr_1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "extra_curr_1"
        return context

#-------------------------------------------------------------------------------------------------
#2]Names of winners at various levels of  sports tournaments
class ExtraCurr2Create(CreateView):
    model = ExtraCurr2
    form_class = ExtraCurr2Form
    template_name = 'create_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Names of winners at various levels of  sports tournaments'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "tab_2"
        context['update_link'] = "extra_curr_2_update"
        context['delete_link'] = "extra_curr_2_delete"
        context['tab_link'] = "extra_curr_tabs.html"
        return context

class ExtraCurr2Update(UpdateView):
    model = ExtraCurr2
    form_class = ExtraCurr2Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Names of winners at various levels of  sports tournaments'
        return context

class ExtraCurr2Delete(DeleteView):
    model = ExtraCurr2
    success_url = reverse_lazy("extra_curr_2")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "extra_curr_2"
        return context
