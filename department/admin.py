from django.contrib import admin
from .models import * 

#Department, StudentResult, DeptProEvent3, DeptFacultyDev4, DeptStudPart5, DeptStartUp6
# Register your models here.
#class UserAdmin(admin.ModelAdmin):

admin.site.register(Department)

admin.site.register(StudentResult)
list_display = ('department','Class','exam_type','subject','date','appeared','passed','perct')

admin.site.register(DeptEvent1)
list_display = ('department','event_type','event_name','guest_name','guest_affl','no_of_part','from_date','to_date')
admin.site.register(DeptEvent2)
list_display = ('act_name','school','school_cont','fac_name','part_no','from_date','to_date')

admin.site.register(DeptProEvent3)
list_display = ('department','activity','resourse_person','resourse_person_contact','no_of_part','from_date','to_date')

admin.site.register(DeptFacultyDev4)
list_display = ('department','program','agency','amm_sponsored','from_date','to_date','no_of_part','level')

admin.site.register(DeptStudPart5)
list_display = ('department','student_name','event_type','event_name','org_inst','from_date','to_date','no_of_part','level','awards')

admin.site.register(DeptStartUp6)
list_display = ('startup_name','startup_nature','start_date','founder','LLP_no','website','team_members')





