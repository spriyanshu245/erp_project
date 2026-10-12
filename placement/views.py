from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AddStudent
from .models import Student


# for Adding and showing new entries
@login_required
def add_show(request):
    if request.method == 'POST':
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added successfully')
            return redirect('show_student')
    else:
        form = AddStudent()

    stud = Student.objects.all()
    return render(request, 'placement/show_student.html', {'form': form, 'stu': stud})


@login_required
def update_data(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = AddStudent(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
            return redirect('show_student')
    else:
        form = AddStudent(instance=student)
    return render(request, 'placement/update_student.html', {'form': form, 'student': student})


@login_required
def delete_data(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        student.delete()
        messages.success(request, 'Deleted successfully')
    return redirect('show_student')
