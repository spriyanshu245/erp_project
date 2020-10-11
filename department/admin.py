from django.contrib import admin
from .models import Student, Department, ProEvent

# Register your models here.

admin.site.register(Department)

admin.site.register(ProEvent)

admin.site.register(Student)
#class UserAdmin(admin.ModelAdmin):
    #list_display = ('id','name','departments','employer','date','package','ref_no')

