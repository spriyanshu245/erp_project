from django.db import models
from datetime import date

DEPARTMENTS = (
    ('Computer Science','Computer Science'),
    ('Electronics and Telecommunication','Electronics and Telecommunication'),
    ('Mechanical','Mechanical'),
    ('Civil','Civil'),
)
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 150,null=False, blank=False)
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='1')
    employer = models.CharField(max_length = 150,null=False, blank=False)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    package = models.IntegerField(null=False, blank=False)
    ref_no = models.IntegerField(null=False, blank=False)
