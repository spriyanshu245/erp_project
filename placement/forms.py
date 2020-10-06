from django.core import validators
from django import forms
from .models import Student


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','department','employer','date','package','ref_no']
        #adding bootstrap classes to form inputs
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'department' : forms.Select(attrs={'class':'form-control'}),
            'employer': forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(format='%m/%d/%Y',attrs={'class':'form-control'}),
            'package': forms.NumberInput(attrs={'class':'form-control'}),
            'ref_no': forms.NumberInput(attrs={'class':'form-control'}),
        }