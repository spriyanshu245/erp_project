from django.contrib import admin
from .models import Student, Department
# Register your models here.

admin.site.register(Department)

@admin.register(Student)    #decorator
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','departments','employer','date','package','ref_no')

