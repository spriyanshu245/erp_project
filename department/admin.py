from django.contrib import admin
from .models import * 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
#class UserAdmin(admin.ModelAdmin):

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

#--------internet


admin.site.register(Profile)
admin.site.register(Department)
admin.site.register(ExtendedUser)


admin.site.register(StudentResult)
list_display = ('department','Class','exam_Type','subject','exam_Date','appeared','passed','percentage')


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


admin.site.register(ResProject1)
admin.site.register(ResFunds2)
admin.site.register(ResInternational3)
admin.site.register(ResNational4)
admin.site.register(ConfInternational5)
admin.site.register(ConfNational6)
admin.site.register(ResIndustrial7)
admin.site.register(FacEvents8)
admin.site.register(ProfessionalPrac9)
admin.site.register(FacPatents10)
admin.site.register(NationalAttend11)
admin.site.register(InternationalAttend12)


admin.site.register(FacAchieve)
admin.site.register(FacBook)


admin.site.register(IndFacvisit1)
admin.site.register(IndInst2)
admin.site.register(IndInst3)
admin.site.register(IndInst4)
admin.site.register(IndInst5)
admin.site.register(IndInst6)
admin.site.register(IndInst7)
admin.site.register(IndInst8)
admin.site.register(IndInst9)


admin.site.register(CurGuestLect1)
admin.site.register(CurExptLect2)
admin.site.register(CurStudTrain3)
admin.site.register(CurStudVisit4)
admin.site.register(CurStudSponsor5)


admin.site.register(StudFac1)
admin.site.register(StudFac2)
admin.site.register(StudFac3)
admin.site.register(StudFac4)
admin.site.register(StudFac5)


admin.site.register(ExtraCurr1)
admin.site.register(ExtraCurr2)
admin.site.register(CulturalCount3)
admin.site.register(CulturalAct3)
admin.site.register(SocialAct4)
admin.site.register(CentersAct5)
admin.site.register(ExtraAct6)


admin.site.register(Ecell)
admin.site.register(EcellCount)


admin.site.register(Placement1)
admin.site.register(Placement2)
admin.site.register(Placement3)
admin.site.register(Placement4)
admin.site.register(Placement5)


admin.site.register(Library1)
admin.site.register(Library2)











