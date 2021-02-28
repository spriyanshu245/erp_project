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

from department.filters import Library1Filter
#------------------------------------------------ LIBRARY VIEWS -----------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#

# Numerical information about library
class Library1Create(CreateView):
    model = Library1
    form_class = Library1Form
    template_name = 'library_custom1.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sheet'] = "library"
        context['header'] = 'Numerical information'
        context['events'] = self.model.objects.all()
        context['nbar'] = "library1_tab"
        context['update_link'] = "library1_update"
        context['delete_link'] = "library1_delete"
        context['tab_link'] = "library_tabs.html"

        context['Library1Filter'] = Library1Filter(self.request.GET, queryset=context['events'])
        context['events'] = context['Library1Filter'].qs
        context['data'] = serializers.serialize( "python", context['events'])[:1]

        if Library2.objects.count() !=4:
            Library2.objects.all().delete()
            Library2.objects.create(details="Number of Faculties Visited",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1, pk=1)
            Library2.objects.create(details="Number of Students Visited",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1, pk=2)
            Library2.objects.create(details="Number of Faculty Transctions",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1, pk=3)
            Library2.objects.create(details="Number of Student Transactions",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1, pk=4)
        else : pass

        context['count_data'] = serializers.serialize( "python", Library2.objects.all() )
        context['count_update'] = "library2_update"
        return context

class Library1Update(UpdateView):
    model = Library1
    form_class = Library1Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Numerical information'
        return context

class Library2Update(UpdateView):
    model = Library2
    form_class = Library2Form
    template_name = "form_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Library Usage'
        return context

class Library1Delete(DeleteView):
    model = Library1
    success_url = reverse_lazy("library1")
    template_name = "form_delete.html"
    context_object_name = "model_instance"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_link'] = "library1"
        return context





# # Numerical information about placement  								
# class Placement1Create(CreateView):
#     model = Placement1
#     form_class = Placement1Form
#     template_name = "placement_custom1.html"


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)   
 
#         context['header'] = 'Numerical information about placement'
#         context['events'] = self.model.objects.all()
#         context['nbar'] = "place1_tab"
#         context['update_link'] = "place1_update"
#         context['delete_link'] = "place1_delete"
#         context['tab_link'] = "placement_tabs.html"
#         context['sheet'] = "placement"

#         context['myFilter'] = Place1Filter(self.request.GET, queryset=context['events'])
#         context['events'] = context['myFilter'].qs
#         context['data'] = serializers.serialize( "python", context['events'])[:1]

#         return context

# class Placement1Update(UpdateView):
#     model = Placement1
#     form_class = Placement1Form
#     template_name = "form_update.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['header'] = 'Numerical information about Placement'
#         return context

# class Placement1Delete(DeleteView):
#     model = Placement1
#     success_url = reverse_lazy("place1")
#     template_name = "form_delete.html"
#     context_object_name = "model_instance"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cancel_link'] = "place1"
#         return context