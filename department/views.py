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
from .forms import *
from .models import *
from .decorators import unauthenticated_user

from department.table_views.department_views import *
from department.table_views.placement_views import *

# Custom templates

# Create your views here.

#------------------------------LOGIN VIEWS-------------------------------------------------------

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + user)
            return redirect("loginPage")

    context = {'form':form}
    return render(request, 'registration/register.html', context)

@unauthenticated_user
def loginPage(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else :
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'registration/loginPage.html', context)
     
    return render(request, 'registration/loginPage.html', context)

def logoutPage(request):
    context = {}
    logout(request)
    return redirect('/loginPage')

#------------------------------TEST PAGE----------------------------------
def testPage(request):
    context = {}
    return render(request, 'registration/register.html', context)





