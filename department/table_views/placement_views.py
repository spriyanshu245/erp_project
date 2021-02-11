from django.views.generic import (CreateView, DetailView, UpdateView, DeleteView)
from django.core import serializers
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from department.forms import *
from department.models import *
from department.decorators import unauthenticated_user

from department.filters import Place1Filter
#------------------------------------------------ PLACEMENT VIEWS -----------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#

# Numerical information about placement  								
class Placement1Create(CreateView):
    model = Placement1
    form_class = Placement1Form
    template_name = "placement_custom1.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
 
        context['header'] = 'Numerical information about placement'
        context['events'] = self.model.objects.all()
        context['years'] = Placement1.objects.values_list('year', flat=True)
        context['data'] = serializers.serialize( "python", self.model.objects.all())
        context['nbar'] = "place1_tab"
        context['update_link'] = "place1_update"
        context['delete_link'] = "place1_delete"
        context['tab_link'] = "placement_tabs.html"

        context['myFilter'] = Place1Filter(self.request.GET, queryset=context['events'])
        context['events'] = context['myFilter'].qs
        context['data'] = serializers.serialize( "python", context['events'])
        # context['testprint'] = print(context['pk_year'])

        return context

class Placement1Update(UpdateView):
    model = Placement1
    form_class = Placement1Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Numerical information about Placement'
        return context

class Placement1Delete(DeleteView):
    model = Placement1
    success_url = reverse_lazy("place1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "place1"
        return context
    
def placement_chart(request):
        labels = []
        data1 = []
        data2 = []

        queryset = Placement1.objects.values().order_by('year')
        for entry in queryset:
            labels.append(entry['year'])
            data1.append(entry['companies_Visited'])
            data2.append(entry['students_Placed'])
        
        return JsonResponse(data={
            'labels': labels,
            'data1': data1,
            'data2': data2,
        })

def salary_chart(request):
        labels = []
        data1 = []
        data2 = []
        data3 = []

        queryset = Placement1.objects.values().order_by('year')
        for entry in queryset:
            labels.append(entry['year'])
            data1.append(entry['max_Salary'])
            data2.append(entry['min_Salary'])
            data3.append(entry['average_Salary'])
        
        return JsonResponse(data={
            'labels': labels,
            'data1': data1,
            'data2': data2,
            'data3': data3,
        })

#-------------------------------------------------------------------------------------------------
# List of companies visited  for campus placement in specified period								
class Placement2Create(CreateView):
    model = Placement2
    form_class = Placement2Form
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of companies visited  for campus placement in specified period'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "place2_tab"
        context['update_link'] = "place2_update"
        context['delete_link'] = "place2_delete"
        context['tab_link'] = "placement_tabs.html"

        # context['count_data'] = serializers.serialize( "python", EcellCount.objects.all() )
        # context['count_update'] = "e_cell_count_update"
        return context

class Placement2Update(UpdateView):
    model = Placement2
    form_class = Placement2Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of companies visited  for campus placement in specified period'
        return context

class Placement2Delete(DeleteView):
    model = Placement2
    success_url = reverse_lazy("place2")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "place2"
        return context

#-------------------------------------------------------------------------------------------------
#List of companies for which students appeared at other campus in specified period								
class Placement3Create(CreateView):
    model = Placement3
    form_class = Placement3Form
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of companies for which students appeared at other campus in specified period'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "place3_tab"
        context['update_link'] = "place3_update"
        context['delete_link'] = "place3_delete"
        context['tab_link'] = "placement_tabs.html"
        return context

class Placement3Update(UpdateView):
    model = Placement3
    form_class = Placement3Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of companies for which students appeared at other campus in specified period'
        return context

class Placement3Delete(DeleteView):
    model = Placement3
    success_url = reverse_lazy("place3")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "place3"
        return context

#--------------------------------------------------------------------------------------
#Student Placement Data								
class Placement4Create(CreateView):
    model = Placement4
    form_class = Placement4Form
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Student Placement Data'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "place4_tab"
        context['update_link'] = "place4_update"
        context['delete_link'] = "place4_delete"
        context['tab_link'] = "placement_tabs.html"
        return context

class Placement4Update(UpdateView):
    model = Placement4
    form_class = Placement4Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Student Placement Data'
        return context

class Placement4Delete(DeleteView):
    model = Placement4
    success_url = reverse_lazy("place4")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "place4"
        return context

#---------------------------------------------------------------------------------------
#List of Students Opted for Entrepreneurship/Self Employment   (During specified period)								
class Placement5Create(CreateView):
    model = Placement5
    form_class = Placement5Form
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of Students Opted for Entrepreneurship/Self Employment (During specified period)'
        context['events'] = self.model.objects.all()
        context['data'] = serializers.serialize( "python", self.model.objects.all() )
        context['nbar'] = "place5_tab"
        context['update_link'] = "place5_update"
        context['delete_link'] = "place5_delete"
        context['tab_link'] = "placement_tabs.html"
        return context

class Placement5Update(UpdateView):
    model = Placement5
    form_class = Placement5Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'List of Students Opted for Entrepreneurship/Self Employment (During specified period)'
        return context

class Placement5Delete(DeleteView):
    model = Placement5
    success_url = reverse_lazy("place5")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "place5"
        return context

