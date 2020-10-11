from django.core import validators
from django import forms
from .models import Student, ProEvent, DeptStudPart

class DateInput(forms.DateInput):
    input_type = 'date'

class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','departments','employer','date','package','ref_no']
        #adding bootstrap classes to form inputs
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'departments' : forms.Select(attrs={'class':'form-control'}),
            'employer': forms.TextInput(attrs={'class':'form-control'}),
            'date' : DateInput(attrs={'class':'form-control'}),
            'package': forms.NumberInput(attrs={'class':'form-control'}),
            'ref_no': forms.NumberInput(attrs={'class':'form-control'}),
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

class AddStudPart(forms.ModelForm):
    class Meta:
        model = DeptStudPart
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