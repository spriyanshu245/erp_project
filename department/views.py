from django.views.generic import (CreateView, DetailView, UpdateView, DeleteView)
from django.core import serializers
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import JsonResponse, request
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from .decorators import unauthenticated_user
from django.http import JsonResponse

from department.table_views.department_views import *
from department.table_views.placement_views import *

from .handler import *
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





################
from django.http import HttpResponse
@login_required
def jsonApiDept(request,title="",stitle="",ttitle=""):
    #request GET:minor filter 
    #UserData = (list(User.objects.filter(id=request.user.id).values('username','id','email','first_name')))+(list(Profile.objects.filter(id=request.user.id).values('dept','role',)))
    #UserData[0] = username id email fname
    #UserData[1] = role dept
    if request.method == "GET":
        pass
    return  HttpResponse(department.STUDENTS_ACADEMIC_PERFORMANCE.getJson(), content_type='application/json')

 

    
    
""" #profile = request.user.get_profile()
    users1 = User.objects.filter(id=request.user.id).values('username','id','email','first_name')
    user2 =  Profile.objects.filter(id=request.user.id).values('dept','role',) #Profilse.objects.filter(request.user.user) 
    #print(user2)
    #role=User.rofile.role  # or simply .values() to get all fields
    users_list = list(users1)
    print(users_list)
    #users_list.append({"role":role}) # important: convert the QuerySet to a list object
    return JsonResponse(users_list, safe=False)
"""    





#############-replica
@login_required
def jsonApiPlace(request,title=None):
    data={"name":h1}
    return JsonResponse(data)


@login_required
def jsonApiLib(request,title=None):
    data={"name":h1}
    return JsonResponse(data)

