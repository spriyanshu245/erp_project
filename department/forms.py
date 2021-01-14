from django.core import validators
from django import forms
from django.db.models.fields import DecimalField
from django.forms.models import ALL_FIELDS
from .models import *
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

# Students Result in various examinations during specified period 
class AddStudentResult(forms.ModelForm):
    class Meta:
        model = StudentResult
        fields = ['department','Class','exam_Type','subject','exam_Date','appeared','passed','percentage']
        #adding bootstrap classes to form inputs
        widgets = {
            'department' : forms.Select(attrs={'class':'form-control'}),
            'Class' : forms.Select(attrs={'class':'form-control'}),
            'exam_Type': forms.Select(attrs={'class':'form-control'}),
            'subject': forms.Select (attrs={'class':'form-control'}),   
            'exam_Date' : DateInput(attrs={'class':'form-control'}),
            'appeared': forms.NumberInput(attrs={'class':'form-control'}),
            'passed': forms.NumberInput(attrs={'class':'form-control'}),
            'percentage': forms.NumberInput(attrs={'class':'form-control'}),
        }


#-------------------------------------------------------------------------------------
                                # DEPARTMENTAL ACTIVITIES

#1] Information about events organized by department
class AddDeptEvent1(forms.ModelForm):
    class Meta:
        model = DeptEvent1
        fields = ['department','event_type','event_name','guest_name','guest_affl','no_of_part','from_date','to_date']
        widgets = {
            'department' : forms.Select(attrs={'class':'form-control'}),
            'event_type': forms.TextInput(attrs={'class':'form-control'}),
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'guest_name': forms.TextInput(attrs={'class':'form-control'}),
            'guest_affl': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
        }

#2] Information about events organized by department (For nearby schools only) 
class AddDeptEvent2(forms.ModelForm):
    class Meta:
        model = DeptEvent2
        fields = ['act_name','school','school_cont','fac_name','part_no','from_date','to_date']
        widgets = {
            'act_name': forms.TextInput(attrs={'class':'form-control'}),
            'school': forms.TextInput(attrs={'class':'form-control'}),
            'school_cont': forms.TextInput(attrs={'class':'form-control'}),
            'fac_name': forms.TextInput(attrs={'class':'form-control'}),
            'part_no': forms.NumberInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
        }

#3] Information about events organized by department in association with Professional bodies
class AddDeptProEvent3(forms.ModelForm):
    class Meta:
        model = DeptProEvent3
        fields = ['department','activity','resourse_person','resourse_person_contact','no_of_part','from_date','to_date']
        #adding bootstrap classes to form inputs
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'activity': forms.TextInput(attrs={'class':'form-control'}),
            'resourse_person': forms.TextInput(attrs={'class':'form-control'}),
            'resourse_person_contact': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}), 
        }

#4] Information about Faculty Development Programs organized by department 
class AddDeptFacultyDev4(forms.ModelForm):
    class Meta:
        model = DeptFacultyDev4
        fields = ['department','program','agency','amm_sponsored','from_date','to_date','no_of_part','level']
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'program' : forms.TextInput(attrs={'class':'form-control'}),
            'agency': forms.TextInput(attrs={'class':'form-control'}),
            'amm_sponsored': forms.NumberInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),
            'level': forms.TextInput(attrs={'class':'form-control'}),
        }

#5] Participation in inter-institute events by students 
class AddDeptStudPart5(forms.ModelForm):
    class Meta:
        model = DeptStudPart5
        fields = ['department','student_name','event_type','event_name','org_inst','from_date','to_date','no_of_part','level','awards']
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'student_name': forms.TextInput(attrs={'class':'form-control'}),
            'event_type' : forms.TextInput(attrs={'class':'form-control'}),
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'org_inst': forms.TextInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),
            'level': forms.TextInput(attrs={'class':'form-control'}),
            'awards': forms.TextInput(attrs={'class':'form-control'}),
        }

#6] Start-Up
class AddDeptStartUp6(forms.ModelForm):
    class Meta:
        model = DeptStartUp6
        fields = ['startup_name','startup_nature','start_date','founder','LLP_no','website','team_members']
        widgets = {
            'startup_name': forms.TextInput(attrs={'class':'form-control'}),
            'startup_nature' : forms.TextInput(attrs={'class':'form-control'}),
            'start_date': DateInput(attrs={'class':'form-control'}),
            'founder': forms.TextInput(attrs={'class':'form-control'}),
            'LLP_no': forms.NumberInput(attrs={'class':'form-control'}),
            'website': forms.URLInput(attrs={'class':'form-control'}),
            'team_members': forms.TextInput(attrs={'class':'form-control'}),
        }


#-------------------------------------------------------------------------------------
                            # FACULTY CONTRIBUTION

#1] Research projects in the specified period
class AddResProject1(forms.ModelForm):
    class Meta:
        model = ResProject1
        fields = ['title','department','name','date','agency','other']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'agency': forms.TextInput(attrs={'class':'form-control'}),
            'other': forms.TextInput(attrs={'class':'form-control'}),
        }

#2] Funds received for research for projects
class AddResFunds2(forms.ModelForm):
    class Meta:
        model = ResFunds2
        fields = ['funding_agency','grants_recieved','grants_utilized','remaining_grant']
        widgets = {
             'funding_agency': forms.TextInput(attrs={'class':'form-control'}),
             'grants_recieved': forms.NumberInput(attrs={'class':'form-control'}),
             'grants_utilized': forms.NumberInput(attrs={'class':'form-control'}),
             'remaining_grant': forms.NumberInput(attrs={'class':'form-control'}),
        }

#3] Research papers published in International journals in the specified period
class AddResInternational3(forms.ModelForm):
    class Meta:
        model = ResInternational3
        fields = ['title','department','authors_name','journal_name','date_of_publication','volume_Issue_ICV','amount','approval','url']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'authors_name': forms.TextInput(attrs={'class':'form-control'}),
            'journal_name': forms.TextInput(attrs={'class':'form-control'}),
            'date_of_publication': DateInput(attrs={'class':'form-control'}),
            'volume_Issue_ICV': forms.TextInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'approval': forms.Select(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
        }

#4] Research papers published in national journals in the specified period
class AddResNational4(forms.ModelForm):
    class Meta:
        model = ResNational4
        fields = ['title','department','authors_name','journal_name','date_of_Publication','volume_Issue_ICV','amount','approval','url']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'authors_name': forms.TextInput(attrs={'class':'form-control'}),
            'journal_name': forms.TextInput(attrs={'class':'form-control'}),
            'date_of_Publication': DateInput(attrs={'class':'form-control'}),
            'volume_Issue_ICV': forms.TextInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'approval': forms.Select(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
        }

#5] Paper presented in International Conferences in the specified periodclass ResNational4(models.Model):
class AddConfInternational5(forms.ModelForm):
    class Meta:
        model = ConfInternational5
        fields = ['title','department','authors_Name','conference_Name','oraganised_by','date','amount','location','url']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'authors_Name': forms.TextInput(attrs={'class':'form-control'}),
            'conference_Name': forms.TextInput(attrs={'class':'form-control'}),
            'oraganised_by': forms.TextInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
        }

#6] Paper presented in National Conferences in the specified period
class AddConfNational6(forms.ModelForm):
    class Meta:
        model = ConfNational6
        fields = ['title','department','authors_Name','conference_Name','oraganised_by','date','amount','location','url']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'authors_Name': forms.TextInput(attrs={'class':'form-control'}),
            'conference_Name': forms.TextInput(attrs={'class':'form-control'}),
            'oraganised_by': forms.TextInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
        }


#7] Research papers authored with industrial persons
class AddResIndustrial7(forms.ModelForm):
    class Meta:
        model = ResIndustrial7
        fields = ['title','authors_Name','co_Author_Name','name_of_Company','date','name_of_Conference_orjournal','location','url']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'authors_Name': forms.TextInput(attrs={'class':'form-control'}),
            'co_Author_Name': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_Company': forms.TextInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'name_of_Conference_orjournal': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
        }

#8] Events for faculty members (FDP/Webinar/Seminar/STTP/Workshops/Others)
class AddFacEvents8(forms.ModelForm):
    class Meta:
        model = FacEvents8
        fields = ['event_Type','event_Name','name_of_Faculty','department','date','level','amount','organising_Institute']
        widgets = {
            'event_Type': forms.TextInput(attrs={'class':'form-control'}),
            'event_Name': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_Faculty': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'level': forms.NumberInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'organising_Institute': forms.TextInput(attrs={'class':'form-control'}),
        }

#9] Participation in Professional Practices (Curriculum Revision/Syllabus Development/Others)
class AddProfessionalPrac9(forms.ModelForm):
    class Meta:
        model = ProfessionalPrac9
        fields = ['faculty_Name','department','professional_Practice_Type','designation','organising_Institute','date']
        widgets = {
            'faculty_Name': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'professional_Practice_Type': forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'organising_Institute': forms.TextInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
        }

#10] List of Faculty Patents/IPR
class AddFacPatents10(forms.ModelForm):
    class Meta:
        model = FacPatents10
        fields = ['faculty_Name','department','invention_Title','patent_Number','date','patent_Status']
        widgets = {
            'faculty_Name': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'invention_Title': forms.TextInput(attrs={'class':'form-control'}),
            'patent_Number': forms.NumberInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'patent_Status': forms.TextInput(attrs={'class':'form-control'}),
        }


#-------------------------------------------------------------------------------------
                                    # FACULTY ACHIEVEMENTS

#1] Faculty Acheivements
class AddFacAchieve(forms.ModelForm):
    class Meta:
        model = FacAchieve
        fields = ['department','fac_name','achievement','level','dates',]
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'fac_name': forms.TextInput(attrs={'class':'form-control'}),
            'achievement': forms.TextInput(attrs={'class':'form-control'}),
            'level': forms.TextInput(attrs={'class':'form-control'}),
            'dates': DateInput(attrs={'class':'form-control'}),
        }


#2] Names of books/Chapters/Manuals/ Monographs published
class AddFacBook(forms.ModelForm):
        class Meta:
            model = FacBook
            fields = ['title','author_name','publication','ISBN']
            widgets = {
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'author_name' : forms.TextInput(attrs={'class':'form-control'}),
                'publication': forms.TextInput(attrs={'class':'form-control'}),
                'ISBN': forms.NumberInput(attrs={'class':'form-control'}),
            }


#--------------------------------------------------------------------------------------------------
                             # INDUSTRY –INSTITUTE INTERACTION

#1]Industrial Visit  of Faculty (Visits accompanied with students should be excluded)
class IndFacVisit1Form(forms.ModelForm):
    class Meta:
        model = IndFacvisit1
        fields = ('faculty','department','company','sector','purpose','from_date','to_date','outcome')
        widgets = {
            'faculty': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'purpose': forms.Textarea(attrs={'rows': 3,'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'outcome': forms.Textarea(attrs={'rows': 3,'class':'form-control'}),
        }

class IndInst2Form(forms.ModelForm):
    class Meta:
        model = IndInst2
        fields = ('name_of_faculty','department','name_of_company','sector','title_of_training','from_date','to_date','outcome')
        widgets = {
            'name_of_faculty': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'name_of_company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'title_of_training': forms.TextInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'outcome': forms.Textarea(attrs={'rows': 3,'class':'form-control'}),
        }

class IndInst3Form(forms.ModelForm):
    class Meta:
        model = IndInst3
        fields = ('name_of_faculty','department','name_of_company','sector','title_of_training','from_date','to_date','outcome')
        widgets = {
            'name_of_faculty': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'name_of_company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'title_of_training': forms.TextInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'outcome': forms.Textarea(attrs={'rows': 3,'class':'form-control'}),
        }

class IndInst4Form(forms.ModelForm):
    class Meta:
        model = IndInst4
        fields = ('name_of_faculty','department','name_of_company','date_of_appointment','type_of_board','designation_of_faculty','meeting_date')
        widgets = {
            'name_of_faculty': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'name_of_company': forms.TextInput(attrs={'class':'form-control'}),
            'date_of_appointment': DateInput(attrs={'class':'form-control'}),
            'type_of_board': forms.TextInput(attrs={'class':'form-control'}),
            'designation_of_faculty': forms.TextInput(attrs={'class':'form-control'}),
            'meeting_date': forms.DateInput(attrs={'class':'form-control'})
        }

class IndInst5Form(forms.ModelForm):
    class Meta:
        model = IndInst5
        fields = ('type_of_board','name_of_industry_member','designation','name_of_company','sector','tenure')
        widgets = {
            'type_of_board': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_industry_member': forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'tenure': forms.TextInput(attrs={'class':'form-control'}),
        }

class IndInst6Form(forms.ModelForm):
    class Meta:
        model = IndInst6
        fields = ('name_of_faculty','title_of_invention','patent_no','date_of_grant','name_of_company','sector','date_of_adoption')
        widgets = {
            'name_of_faculty': forms.TextInput(attrs={'class':'form-control'}),
            'title_of_invention': forms.TextInput(attrs={'class':'form-control'}),
            'patent_no': forms.TextInput(attrs={'class':'form-control'}),
            'date_of_grant': DateInput(attrs={'class':'form-control'}),
            'name_of_company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.Select(attrs={'class':'form-control'}),
            'date_of_adoption': DateInput(attrs={'class':'form-control'}),
            }

class IndInst7Form(forms.ModelForm):
    class Meta:
        model = IndInst7
        fields = ('title_of_project','name_of_coordinator','name_of_sponsoring_company','duration_from','duration_to','grant_received','status_of_project')
        widgets = {
            'title_of_project': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_coordinator': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_sponsoring_company': forms.TextInput(attrs={'class':'form-control'}),
            'duration_from': DateInput(attrs={'class':'form-control'}),
            'duration_to': DateInput(attrs={'class':'form-control'}),
            'grant_received': forms.Select(attrs={'class':'form-control'}),
            'status_of_project': forms.TextInput(attrs={'class':'form-control'}),
        }

class IndInst8Form(forms.ModelForm):
    class Meta:
        model = IndInst8
        fields = ('name_of_faculty','name_of_company','title_of_project','revenue_generated','dates_from','dates_to','status_of_project')
        widgets = {
            'name_of_faculty': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_company': forms.TextInput(attrs={'class':'form-control'}),
            'title_of_project': forms.TextInput(attrs={'class':'form-control'}),
            'revenue_generated': forms.NumberInput(attrs={'class': 'form-control'}),
            'dates_from': DateInput(attrs={'class':'form-control'}),
            'dates_to': DateInput(attrs={'class':'form-control'}),
            'status_of_project': forms.TextInput(attrs={'class':'form-control'}),
        }

class IndInst9Form(forms.ModelForm):
    class Meta:
        model = IndInst9
        fields = ('department','name_of_faculty_coordinator','name_of_company','sector','date_of_MOU','purpose_of_MOU')
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'name_of_faculty_coordinator': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.Select(attrs={'class':'form-control'}),
            'date_of_MOU': DateInput(attrs={'class':'form-control'}),
            'purpose_of_MOU': forms.TextInput(attrs={'class':'form-control'}),
        }


#-----------------------------------------------------------------------------------------
                               # CURRICULUM INPUT

#1] Guest Lectures (General Topics)
class AddCurGuestLect1(forms.ModelForm):
    class Meta:
        model = CurGuestLect1
        fields = ['guest','organization','designation','topic','department','date','no_of_part']
        widgets = {
            'guest': forms.TextInput(attrs={'class':'form-control'}),
            'organization' : forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'topic': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),
        }

            
#2] Expert Lectures (Subject-Specific Topics)
class AddCurExptLect2(forms.ModelForm):
    class Meta:
        model = CurExptLect2
        fields = ['guest','organization','designation','topic','department','date','no_of_part']
        widgets = {
            'guest': forms.TextInput(attrs={'class':'form-control'}),
            'organization' : forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'topic': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),
        }


#3] Student Internship/Industrial Training 
class AddCurStudTrain3(forms.ModelForm):
    class Meta:
        model = CurStudTrain3
        fields = ['department','student_name','company','sector','from_date','to_date']
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'student_name': forms.TextInput(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
        }


#4] Student Industrial Visit 
class AddCurStudVisit4(forms.ModelForm):
    class Meta:
        model = CurStudVisit4
        fields = ['department','company','sector','fac_name','no_of_stud','from_date','to_date']
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'fac_name': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_stud': forms.NumberInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
        }

#5] Students Sponsored Projects
class AddCurStudSponsor5(forms.ModelForm):
    class Meta:
        model = CurStudSponsor5
        fields = ['title','comp_rep','comp_sponsor','from_date','to_date','grant','status']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'comp_rep': forms.TextInput(attrs={'class':'form-control'}),
            'comp_sponsor': forms.TextInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'grant': forms.Select(attrs={'class':'form-control'}),
            'status': forms.TextInput(attrs={'class':'form-control'}),
        }


#--------------------------------------------------------------------------------------------------
# STUDENT /FACULTY SUPPORT SYSTEM
class StudFac1Form(forms.ModelForm):
    class Meta:
        model = StudFac1
        fields = ('department','class_or_division','type_of_meeting_open_GFM_or_HOD_close','name_of_faculty','type_of_mentoring','dates_of_mentoring_activity')
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'class_or_division': forms.TextInput(attrs={'class':'form-control'}),
            'type_of_meeting_open_GFM_or_HOD_close': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_faculty': forms.TextInput(attrs={'class':'form-control'}),
            'type_of_mentoring': forms.TextInput(attrs={'class':'form-control'}), 
            'dates_of_mentoring_activity': forms.TextInput(attrs={'class':'form-control'}),
        }

class StudFac2Form(forms.ModelForm):
    class Meta:
        model = StudFac2
        fields = ("class_or_division","type_of_self_learning_facility","name_of_subject","no_of_student_participated","dates","certificate_or_award_received_by_students")
        widgets = {
            "class_or_division": forms.TextInput(attrs={'class':'form-control'}),
            "type_of_self_learning_facility": forms.Select(attrs={'class':'form-control'}),
            "name_of_subject": forms.TextInput(attrs={'class':'form-control'}),
            "no_of_student_participated": forms.NumberInput(attrs={'class': 'form-control'}),
            "dates": forms.TextInput(attrs={'class':'form-control'}),
            "certificate_or_award_received_by_students": forms.TextInput(attrs={'class':'form-control'}),
        }

class StudFac3Form(forms.ModelForm):
    class Meta:
        model = StudFac3
        fields = ("name_of_student","department","name_of_competitive_exam_appeard_or_qualified","competitive_exam_seat_no","score")
        widgets = {
            "name_of_student": forms.TextInput(attrs={'class':'form-control'}),
            "department": forms.Select(attrs={'class':'form-control'}),
            "name_of_competitive_exam_appeard_or_qualified": forms.Select(attrs={'class':'form-control'}),
            "competitive_exam_seat_no": forms.TextInput(attrs={'class':'form-control'}),
            "score": forms.NumberInput(attrs={'class': 'form-control'}),
            
        }

class StudFac4Form(forms.ModelForm):
    class Meta:
        model = StudFac4
        fields = ("name_of_activity","date_of_implementation","no_of_students_enrolled","agencies_involved")
        widgets = {
            "name_of_activity": forms.Select(attrs={'class':'form-control'}),
            "date_of_implementation": DateInput(attrs={'class':'form-control'}),
            "no_of_students_enrolled": forms.NumberInput(attrs={'class':'form-control'}),
            "agencies_involved": forms.TextInput(attrs={'class':'form-control'}),
        }

class StudFac5Form(forms.ModelForm):
    class Meta:
        model = StudFac5
        fields = ("title_of_the_professional_development_program","organized_for_faculty_or_staff","organizing_department","duration_open_from_close","duration_open_to_close","no_of_participants","agencies_involved")
        widgets = {
            "title_of_the_professional_development_program": forms.TextInput(attrs={'class':'form-control'}),
            "organized_for_faculty_or_staff": forms.TextInput(attrs={'class':'form-control'}),
            "organizing_department": forms.Select(attrs={'class':'form-control'}),
            "duration_open_from_close": DateInput(attrs={'class':'form-control'}),
            "duration_open_to_close": DateInput(attrs={'class':'form-control'}),
            "no_of_participants": forms.NumberInput(attrs={'class':'form-control'}),
            "agencies_involved": forms.TextInput(attrs={'class':'form-control'}),
        }

#--------------------------------------------------------------------------------------------------
# EXTRA CURRICULAR ACTIVITIES
class ExtraCurr1Form(forms.ModelForm):
    class Meta:
        model = ExtraCurr1
        fields = ("activity","organized_by","level","date","number_of_students_participated")
        widgets = {
            "activity": forms.TextInput(attrs={'class': 'form-control'}),
            "organized_by": forms.TextInput(attrs={'class': 'form-control'}),
            "level": forms.TextInput(attrs={'class': 'form-control'}),
            "date": DateInput(attrs={'class':'form-control'}),
            "number_of_students_participated": forms.NumberInput(attrs={'class':'form-control'}),
        }

class ExtraCurr2Form(forms.ModelForm):
    class Meta:
        model = ExtraCurr2
        fields = ("name_of_the_sport_or_team","student_ID_number","name_of_department","level","rank")
        widgets = {
            "name_of_the_sport_or_team": forms.TextInput(attrs={'class': 'form-control'}),
            "student_ID_number": forms.TextInput(attrs={'class': 'form-control'}),
            "name_of_department": forms.Select(attrs={'class':'form-control'}),
            "level": forms.TextInput(attrs={'class': 'form-control'}),
            "rank": forms.NumberInput(attrs={'class':'form-control'}),
        }



#------------------------------user----------------------------------------------------------------
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('role', 'dept')
