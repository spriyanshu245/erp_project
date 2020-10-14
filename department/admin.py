from django.contrib import admin
from .models import * 

#Department, StudentResult, DeptProEvent3, DeptFacultyDev4, DeptStudPart5, DeptStartUp6
# Register your models here.
#class UserAdmin(admin.ModelAdmin):

admin.site.register(Department)

admin.site.register(StudentResult)
list_display = ('department','Class','exam_type','subject','exam_date','appeared','passed','perct')

admin.site.register(DeptProEvent3)
list_display = ('department','activity_name','resourse_person_name','resourse_person_contact','no_of_participants','event_from_date','event_to_date')

admin.site.register(DeptFacultyDev4)
list_display = ('department','program_name','sponsor_agency','sponsored_amount','from_date','to_date','no_of_participants','level')

admin.site.register(DeptStudPart5)
list_display = ('department','student_name','event_type','event_name','organising_institute','from_date','to_date','no_of_participants','level','awards')

admin.site.register(DeptStartUp6)
list_display = ('student_name','startup_nature','commencement_date','founder_name','LLP_number','website','team_members')





