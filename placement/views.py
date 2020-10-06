from django.shortcuts import render, HttpResponseRedirect
from .forms import AddStudent
from .models import Student
from django.contrib import messages

# Create your views here.
# for Adding and showing new entrys
def add_show(request):
    form = AddStudent(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            nm = cd['name']
            dp = cd['department']
            em = cd['employer']
            dt = cd['date']
            pk = cd['package']
            rf = cd['ref_no']
            #model class object created (reg)
            reg = Student(name=nm, department=dp, employer=em,date=dt, package=pk, ref_no=rf)
            reg.save()
            messages.success(request, 'Added successfully')
            return HttpResponseRedirect('/')
        form = AddStudent() 
    else:
        form = AddStudent()

    stud = Student.objects.all()
    return render(request, 'placement/show_student.html',{'form':form,'stu':stud})

def delete_data(request, id):
    if request.method == 'POST' :
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
