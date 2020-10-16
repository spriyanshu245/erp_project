from django.core import validators
from django import forms
<<<<<<< HEAD
from .models import *
# StudentResult, DeptEvent1, DeptEvent2, DeptProEvent3, DeptFacultyDev4, DeptStudPart5, DeptStartUp6, FacBook, GuestLect1, ExptLect2
=======
# from .models import CurStudTrain3, FacAchieve, StudentResult, DeptEvent1, DeptEvent2, DeptProEvent3, DeptFacultyDev4, DeptStudPart5, DeptStartUp6
from .models import *
>>>>>>> 4e0485afc6bd31dbc0c2cace985e92bdec2a06dd

class DateInput(forms.DateInput):
    input_type = 'date'

# Students Result in various examinations during specified period 
class AddStudentResult(forms.ModelForm):
    class Meta:
        model = StudentResult
        fields = ['department','Class','exam_type','subject','date','appeared','passed','perct']
        #adding bootstrap classes to form inputs
        widgets = {
            'department' : forms.Select(attrs={'class':'form-control'}),
            'Class' : forms.Select(attrs={'class':'form-control'}),
            'exam_type': forms.Select(attrs={'class':'form-control'}),
            'subject': forms.Select (attrs={'class':'form-control'}),   
            'date' : DateInput(attrs={'class':'form-control'}),
            'appeared': forms.NumberInput(attrs={'class':'form-control'}),
            'passed': forms.NumberInput(attrs={'class':'form-control'}),
            'perct': forms.NumberInput(attrs={'class':'form-control'}),
        }
#-------------------------------------------------------------------------------------

#1 Information about events organized by department
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

#2 Information about events organized by department (For nearby schools only) 
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

#3 Information about events organized by department in association with Professional bodies
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


#4 Information about Faculty Development Programs organized by department 
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


#5 Participation in inter-institute events by students 
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


#6 Start-Up
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
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'team_members': forms.TextInput(attrs={'class':'form-control'}),
        }
#-------------------------------------------------------------------------------------
                # Form space for faculty contribution tables

#-------------------------------------------------------------------------------------

#2 Names of books/Chapters/Manuals/ Monographs published
class AddFacBook(forms.ModelForm):
        class Meta:
            model = FacBook
            fields = ['title','author_name','start_date','founder','LLP_no','website','team_members']
            widgets = {
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'author_name' : forms.TextInput(attrs={'class':'form-control'}),
                'publication': forms.TextInput(attrs={'class':'form-control'}),
                'ISBN': forms.NumberInput(attrs={'class':'form-control'}),
            }

#-------------------------------------------------------------------------------------

#1 Guest Lectures (General Topics)
class AddGuestLect1(forms.ModelForm):
    class Meta:
        model = GuestLect1
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

            
#2 Expert Lectures (Subject-Specific Topics)
class AddExptLect2(forms.ModelForm):
    class Meta:
        model = ExptLect2
        fields = ['guest','organization','designation','topic','department','date','no_of_part']
        widgets = {
            'guest': forms.TextInput(attrs={'class':'form-control'}),
            'organization' : forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'topic': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),

## Faculty Acheivements ----------------------------------------------------
#1 Faculty Acheivements
class AddFacAchievements(forms.ModelForm):
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

## Curriculum Input
#3 Student Internship/Industrial Training 
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

#4 Student Industrial Visit 
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

#5 Students Sponsored Projects
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