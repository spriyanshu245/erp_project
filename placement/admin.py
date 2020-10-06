from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student) #decorator
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','department','employer','date','package','ref_no')

