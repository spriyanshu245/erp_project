from django.db import models
from datetime import date

DEPARTMENTS = (
    ('Computer Science','Computer Science'),
    ('Electronics and Telecommunication','Electronics and Telecommunication'),
    ('Mechanical','Mechanical'),
    ('Civil','Civil'),
)
# Create your models here.

class Department(models.Model):
    department = models.CharField(primary_key=True, max_length=128)

    def __str__(self):
        return self.department

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 150,null=False, blank=False)
    departments = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    # departments = models.ForeignKey(Department, on_delete=models.CASCADE)
    employer = models.CharField(max_length = 150,null=False, blank=False)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    package = models.IntegerField(null=False, blank=False)
    ref_no = models.IntegerField(null=False, blank=False)
    objects = models.Manager()

class ProEvent(models.Model):
    no = models.IntegerField()
    activity = models.CharField(max_length=150)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    pname = models.CharField(max_length=150)
    pcontact = models.IntegerField()
    participants = models.IntegerField()
    fromdate = models.DateField(("Date"), auto_now=False, auto_now_add=False)
    todate = models.DateField(("Date"), auto_now=False, auto_now_add=False)



