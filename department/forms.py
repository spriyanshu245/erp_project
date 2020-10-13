from django.core import validators
from django import forms
from .models import StudentResult, DeptProEvent3, DeptFacultyDev4, DeptStudPart5, DeptStartUp6

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
            'percentage': forms.NumberInput(attrs={'class':'form-control'}),
        }


#3 Information about events organized by department in association with Professional bodies
class AddDeptProEvent3(forms.ModelForm):
    class Meta:
        model = DeptProEvent3
        fields = ['department','activity','resourse_person','resourse_person_contact','no_of_part','from_date','to_date']
        #adding bootstrap classes to form inputs
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'activity_name': forms.TextInput(attrs={'class':'form-control'}),
            'resourse_person_name': forms.TextInput(attrs={'class':'form-control'}),
            'resourse_person_contact': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_participants': forms.NumberInput(attrs={'class':'form-control'}),
            'event_from_date': DateInput(attrs={'class':'form-control'}),
            'event_to_date': DateInput(attrs={'class':'form-control'}) 
        }


#4 Information about Faculty Development Programs organized by department 
class AddDeptFacultyDev4(forms.ModelForm):
    class Meta:
        model = DeptFacultyDev4
        fields = ['department','program','agency','amm_sponsored','from_date','to_date','no_of_part','level']
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'program_name' : forms.TextInput(attrs={'class':'form-control'}),
            'sponsor_agency': forms.TextInput(attrs={'class':'form-control'}),
            'sponsored_amount': forms.NumberInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'no_of_participants': forms.NumberInput(attrs={'class':'form-control'}),
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
            'organising_institute': forms.TextInput(attrs={'class':'form-control'}),
            'from_date': DateInput(attrs={'class':'form-control'}),
            'to_date': DateInput(attrs={'class':'form-control'}),
            'no_of_participants': forms.NumberInput(attrs={'class':'form-control'}),
            'level': forms.TextInput(attrs={'class':'form-control'}),
        }


#6 Start-Up
class AddDeptStartUp6(forms.ModelForm):
    class Meta:
        model = DeptStartUp6
        fields = ['startup_name','startup_nature','start_date','founder','LLP_no','website','team_members']
        widgets = {
            'startup_name': forms.TextInput(attrs={'class':'form-control'}),
            'startup_nature' : forms.TextInput(attrs={'class':'form-control'}),
            'commencement_date': DateInput(attrs={'class':'form-control'}),
            'founder_name': forms.TextInput(attrs={'class':'form-control'}),
            'LLP_number': forms.NumberInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'team_members': forms.TextInput(attrs={'class':'form-control'}),
        }
