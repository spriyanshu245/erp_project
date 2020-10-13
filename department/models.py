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
    department = models.CharField(primary_key=True, max_length=128,unique=True)

    def __str__(self):
        return self.department

class StudentNew(models.Model):
    # id               = models.AutoField(primary_key=True)
    name             = models.CharField(max_length = 150,null=False, blank=False)
    departments      = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    # departments    = models.ForeignKey(Department, on_delete=models.CASCADE)
    employer         = models.CharField(max_length = 150,null=False, blank=False)
    date             = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    package          = models.IntegerField(null=False, blank=False)
    ref_no           = models.IntegerField(null=False, blank=False)
    year_admission   = models.IntegerField(default=0)
    #year of addmission 
    year_down        = models.IntegerField(default=0)
    # class calculation class=  currunt year - (year admission + year down) month june is middle factor
    # objects          = models.Manager()

#Information about events organized by department in association with Professional bodies
class ProEvent(models.Model):
    activity_name = models.CharField(max_length=150)
    department_name = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    #department_name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    resourse_person_name = models.CharField(max_length=150)
    resourse_person_contact = models.IntegerField()
    no_of_participants = models.IntegerField()
    event_from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    event_to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    objects = models.Manager()

    def __str__(self):
        return self.activity_name

#Participation in inter-institute events by students 
class DeptStudPart5(models.Model):
    student_name = models.CharField(max_length=150)
    event_type = models.CharField(max_length=150)
    event_name = models.CharField(max_length=150)
    org_inst = models.CharField(max_length=264)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)
    awards = models.CharField(("Recognition Awards"), max_length=264)

#Information about Faculty Development Programs organized by department 
class FacultyDevProOrg_Dep(models.Model):
    program_name = models.CharField(max_length=150)
    department_name = models.CharField(max_length=150)
    sponsoring_agency = models.CharField(max_length=150)
    amm_sponsored = models.IntegerField(default=0)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)



#Start-Up
class DeptStartUp6(models.Model):
    startup_name = models.CharField(max_length=150)
    nature_startup = models.CharField(max_length=150)
    date_commencement = models.DateField(default=date.today,auto_now=False, auto_now_add=False)
    #TODO ^
    founder = models.CharField(max_length=150)
    LLP_no = models.IntegerField()
    startup_web = models.CharField(max_length=150)
    team_members = models.CharField( max_length=500)
    #team_member isnt right



