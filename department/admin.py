from django.contrib import admin
from .models import Student, Department, ProEvent, DeptStudPart

# Register your models here.
#class UserAdmin(admin.ModelAdmin):

admin.site.register(Department)

admin.site.register(Student)
list_display = ('department','Class','exam_type','subject','date','appeared','passed','perct')

admin.site.register(ProEvent)
list_display = ('activity_name','department_name','resourse_person_name','resourse_person_contact','no_of_participants','event_from_date','event_to_date')

admin.site.register(DeptStudPart)
list_display = ('student_name','event_type','event_name','org_inst','from_date','to_date','no_of_part','level','awards')



