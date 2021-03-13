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
from .decorators import unauthenticated_user

from .models import *
from .forms import *
from department.table_views.department_views import *
from department.table_views.placement_views import *


from django.http import HttpResponse
from .handler import *
from django.shortcuts import render
from django.template import RequestContext
# Custom templates

# Create your views here.

#------------------------------LOGIN VIEWS-------------------------------------------------------

def registerPage(request):

    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            print(user.username)
            messages.success(request, 'Account successfully created for ' + user.username ) #Add user.username here
            return redirect("register")

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {
        'form':form,
        'profile_form':profile_form,
    }

    return render(request, 'registration/register.html', context)

@unauthenticated_user
def loginPage(request):
    context = {}

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        
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
def testRegisterPage(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Account successfully created for ' + user.username)
            return redirect("test2")

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {
        'form':form,
        'profile_form':profile_form,
    }

    return render(request, 'test2.html', context)

def test2(request):
    context = {}
    return render(request, 'test2.html', context)

#------------------------About us --------------------------
def aboutus(request):
    return render(request,'about_us.html/')

############JsonAPi
@login_required
def jsonApiDept(request,title=0,stitle=0,ttitle=0):
    if request.method == "GET":
        formate = request.GET.get('format') or "json"
    if formate == "json":
        data = getAllXls(2).getvalue()
        response =JsonResponse(json.loads(data),safe=False)
    elif formate == "xls":
        data = getAllXls(1).getvalue()
        response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=dept%s.xlsx' % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    return response 
@login_required
def ProfileApi(request,username):
    if request.user.username != username :
        pass
        #return HttpResponse(status=401)
    #TODO update as per User model
    ProfileData = list(User.objects.filter(id=request.user.id).values('username','id','email','first_name'))+list(Profile.objects.filter(id=request.user.id).values('dept','role',))
    print (ProfileData)
    return JsonResponse(ProfileData,safe=False)

#404


def handler404(request, *args, **argv):
    print ('lol')
    response = HttpResponse('404.html')
    response.status_code = 404
    return response
