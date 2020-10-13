from django.core import validators
from django import forms
from .models import StudentNew, ProEvent,DeptFacDevProg4, DeptStudPart5, DeptStartUp6, DeptEvent2

class DateInput(forms.DateInput):
    input_type = 'date'

class AddStudentNew(forms.ModelForm):
    class Meta:
        model = StudentNew
        fields = ['name','departments','employer','date','package','ref_no','year_admission','year_down']
        #adding bootstrap classes to form inputs
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'departments' : forms.Select(attrs={'class':'form-control'}),
            'employer': forms.TextInput(attrs={'class':'form-control'}),
            'date' : DateInput(attrs={'class':'form-control'}),
            'package': forms.NumberInput(attrs={'class':'form-control'}),
            'ref_no': forms.NumberInput(attrs={'class':'form-control'}),
            'year_admission': forms.NumberInput(attrs={'class':'form-control'}),
            'year_down': forms.NumberInput(attrs={'class':'form-control'}),
        }

class AddProEvent(forms.ModelForm):
    class Meta:
        model = ProEvent
        fields = ['activity_name','department_name','resourse_person_name','resourse_person_contact','no_of_participants','event_from_date','event_to_date']
        #adding bootstrap classes to form inputs
        widgets = {
            'activity_name': forms.TextInput(attrs={'class':'form-control'}),
            'department_name': forms.Select(attrs={'class':'form-control'}),
            'resourse_person_name': forms.TextInput(attrs={'class':'form-control'}),
            'resourse_person_contact': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_participants': forms.NumberInput(attrs={'class':'form-control'}),
            'event_from_date': DateInput(attrs={'class':'form-control'}),
            'event_to_date': DateInput(attrs={'class':'form-control'}) 
        }

class AddStudPart5(forms.ModelForm):
    class Meta:
        model = DeptStudPart5
        fields = ['student_name','event_type','event_name','org_inst','from_date','to_date','no_of_part','level','awards']
        widgets = {
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


#Information about Faculty Development Programs organized by department 
class AddFacDevProg4(forms.ModelForm):
    class Meta:
        model = DeptFacDevProg4
        fields = ['program_name','department_name','sponsoring_agency','amt_sponsored','from_date','to_date','no_of_part','level']
        widgets = {
            'program_name': forms.TextInput(attrs={'class':'form-control'}),
            'department_name' : forms.TextInput(attrs={'class':'form-control'}),
            'sponsoring_agency': forms.TextInput(attrs={'class':'form-control'}),
            'amt_sponsored': forms.NumberInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'no_of_part': forms.NumberInput(attrs={'class':'form-control'}),
            'level': forms.TextInput(attrs={'class':'form-control'}),
        }


class AddStartUp6(forms.ModelForm):
    class Meta:
        model = DeptStartUp6
        fields = ['startup_name','nature_startup','date_commencement','founder','LLP_no','startup_web','team_members']
        widgets = {
            'startup_name': forms.TextInput(attrs={'class':'form-control'}),
            'nature_startup' : forms.TextInput(attrs={'class':'form-control'}),
            'date_commencement': forms.DateInput(attrs={'class':'form-control'}),
            'founder': forms.TextInput(attrs={'class':'form-control'}),
            'LLP_no': forms.NumberInput(attrs={'class':'form-control'}),
            'startup_web': forms.TextInput(attrs={'class':'form-control'}),
            'team_members': forms.TextInput(attrs={'class':'form-control'}),
        }

class AddEvent2(forms.ModelForm):
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
