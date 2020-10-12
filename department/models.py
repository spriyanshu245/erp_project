from django.db import models
from datetime import date

DEPARTMENTS = (
    ('Computer Science','Computer Science'),
    ('Electronics and Telecommunication','Electronics and Telecommunication'),
    ('Mechanical','Mechanical'),
    ('Civil','Civil'),
)
CLASS = (
    ('SE','SE'),
    ('TE','TE'),
    ('BE','BE'),
)

# Create your models here.

class Department(models.Model):
    department = models.CharField(primary_key=True, max_length=128,unique=True)

    def __str__(self):
        return self.department

class Student(models.Model):
    
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    Class = models.CharField(max_length = 150, choices=CLASS, default='none',null=False, blank=False)
    #department = models.ForeignKey(Department, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length = 150,null=False, blank=False)
    subject = models.CharField(max_length = 150,null=False, blank=False)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    appeared = models.IntegerField(null=False, blank=False)
    passed = models.IntegerField(null=False, blank=False)
    perct = models.IntegerField(null=False, blank=False)
    objects = models.Manager()

class ProEvent(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    activity_name = models.CharField(max_length=150)
    department_name = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    #department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    resourse_person_name = models.CharField(max_length=150)
    resourse_person_contact = models.IntegerField()
    no_of_participants = models.IntegerField()
    event_from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    event_to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    objects = models.Manager()

    def __str__(self):
        return self.activity_name

class DeptStudPart(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    student_name = models.CharField(max_length=150)
    event_type = models.CharField(max_length=150)
    event_name = models.CharField(max_length=150)
    org_inst = models.CharField(max_length=264)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)
    awards = models.CharField(("Recognition Awards"), max_length=264)