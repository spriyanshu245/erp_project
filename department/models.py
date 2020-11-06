from django.db import models
from datetime import date
from .choices import DEPARTMENTS, CLASS, EXAM_TYPES, SUBJECTS, GRANT, ROLE, DEPT_PEM, SECTOR
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

# Models with Primary Keys
## remaining --designation,
class Department(models.Model):
    department = models.CharField(("Department Name"),primary_key=True, max_length=128,unique=True)

    def __str__(self):
        return self.department

class Sector(models.Model):
    sector = models.CharField(max_length=150)

    def __str__(self):
        return self.sector

#-------------------------------------------------------------------------------------
# Students Result in various examinations during specified period 
class StudentResult(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    Class = models.CharField(max_length = 150, choices=CLASS, default='')
    #department = models.ForeignKey(Department, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length = 150, choices=EXAM_TYPES, default='')
    subject = models.CharField(max_length = 150, choices=SUBJECTS, default='')
    date = models.DateField(("Exam Date"), default=date.today,auto_now=False, auto_now_add=False)
    appeared = models.IntegerField(null=False, blank=False)
    passed = models.IntegerField(null=False, blank=False)
    perct = models.IntegerField(("Percentage"),default=0,null=False, blank=False)
    objects = models.Manager()

#-------------------------------------------------------------------------------------
#1 Information about events organized by department
class DeptEvent1(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    event_type = models.CharField(("Event Type"),max_length=150)
    event_name = models.CharField(("Event Name"),max_length=150)
    guest_name = models.CharField(("Guest Name"),max_length=150)
    guest_affl = models.CharField(("Affiliation of guest"),max_length=250)
    no_of_part = models.IntegerField(("No of Participants"))
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)

#2 Information about events organized by department (For nearby schools only)
class DeptEvent2(models.Model):
    act_name = models.CharField(("Activity Name"),max_length=150)
    school = models.CharField(max_length=150)
    school_cont = models.CharField(("School Contact Details"),max_length=250)
    fac_name = models.CharField(("Faculty Name"),max_length=250)
    part_no = models.IntegerField(("No of Participants"))
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)

#3 Information about events organized by department in association with Professional bodies
class DeptProEvent3(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    activity = models.CharField(max_length=150)
    #department_name = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    #department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    resourse_person = models.CharField(max_length=150)
    resourse_person_contact = models.IntegerField()
    no_of_part = models.IntegerField(("No of Participants"))
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    objects = models.Manager()

    def __str__(self):
        return self.activity

#4 Information about Faculty Development Programs organized by department 
class DeptFacultyDev4(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    program = models.CharField(max_length=150)
    agency = models.CharField(max_length=150)
    amm_sponsored = models.IntegerField(default=0)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)

#5 Participation in inter-institute events by students 
class DeptStudPart5(models.Model):
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

#6 Start-Up
class DeptStartUp6(models.Model):
    startup_name = models.CharField(max_length=150)
    startup_nature = models.CharField(max_length=150)
    start_date = models.CharField(("Commencement Date"),max_length=150)
    founder = models.CharField(max_length=150)
    LLP_no = models.IntegerField(("LLP number"))
    website = models.CharField(max_length=150)
    team_members = models.CharField(max_length=500)

#-------------------------------------------------------------------------------------
                # Model space for faculty contribution tables

#-------------------------------------------------------------------------------------
#1 Faculty achievements
class FacAchieve(models.Model):
    fac_name = models.CharField(("Faculty Name"), max_length=150)
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    achievement = models.CharField(max_length=150)
    level = models.CharField(max_length=150)
    dates = models.DateField(("Dates"), default=date.today,auto_now=False, auto_now_add=False)

#2 Names of books/Chapters/Manuals/ Monographs published
class FacBook(models.Model):
    title = models.CharField(("Title"),max_length=500)
    author_name = models.CharField(("Name of author(s)"),max_length=150)
    publication = models.CharField(("Publication"),max_length=150)
    ISBN = models.IntegerField(("ISBN number"))

#-------------------------------------------------------------------------------------
                          # CURRICULUM INPUT
#1 Guest Lectures (General Topics)
class CurGuestLect1(models.Model):
    guest = models.CharField(("Name of Guest"),max_length = 150)
    organization = models.CharField(("Company/Organization Represented"),max_length=150)
    designation = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    department = models.CharField(("Name of Organizing Department"), max_length = 150, choices=DEPARTMENTS)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))

#2 Expert Lectures (Subject-Specific Topics)
class CurExptLect2(models.Model):
    guest = models.CharField(("Name of Guest"),max_length = 150)
    organization = models.CharField(("Company/Organization Represented"),max_length=150)
    designation = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    department = models.CharField(("Name of Organizing Department"), max_length = 250, choices=DEPARTMENTS)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))

# class ExptLect2(GuestLect1):
#     pass
  
#3 Student Internship/Industrial training
class CurStudTrain3(models.Model):
    # No	Name of Department	Name of Student		Name of Company		Sector		Date/Duration
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    student_name = models.CharField(("Name of Student"), max_length=150)
    company = models.CharField(("Name of Company"), max_length=250)
    sector = models.CharField(max_length=250)
    from_date = models.DateField(("Duration (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Duration (To)"), default=date.today,auto_now=False, auto_now_add=False)

#4 Student Industrial Visit
class CurStudVisit4(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    company = models.CharField(("Name of Company"), max_length=250)
    sector = models.CharField(max_length=250)
    fac_name = models.CharField(("Faculty Name"),max_length=150)
    no_of_stud = models.IntegerField(("No of Students"))
    from_date = models.DateField(("Duration (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Duration (To)"), default=date.today,auto_now=False, auto_now_add=False)

# Student Sponsored Projects
class CurStudSponsor5(models.Model):
    title = models.CharField(("Title of Project"),max_length=250)
    comp_rep = models.CharField(("Name of Company Representative"), max_length=250)
    comp_sponsor = models.CharField(("Name of Sponsoring company"), max_length=250)
    from_date = models.DateField(("Duration (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Duration (To)"), default=date.today,auto_now=False, auto_now_add=False)
    grant = models.CharField(("Grant Received"), max_length=150, choices=GRANT, default='No')
    status = models.CharField(max_length=150)

# class MY_CHOICES(models.Model)
#     choice = models.CharField(max_length=154, unique=True)

# class MODEL(models.Model):
#     ...
#     ...
#     my_field = models.ManyToManyField(MY_CHOICES)
    
#-----------------------------------------------------------------
# INDUSTRY –INSTITUTE INTERACTION

#1]Industrial Visit  of Faculty (Visits accompanied with students should be excluded)
class IndFacvisit1(models.Model):
    faculty = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.CharField("Name of Company", max_length=256)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    purpose = models.TextField()
    from_date = models.DateField(("Dates (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Dates (To)"), default=date.today,auto_now=False, auto_now_add=False)
    outcome = models.TextField()

    def __str__(self):
        return self.faculty

    def get_absolute_url(self):
        return reverse('ind_inst_1',)

#2] Training  of Faculty by Industry
class IndInst2(models.Model):
    # No	Name of Faculty	Name of Department	Name of Company 		*Sector	Title of Training	Dates	Outcome
    name_of_faculty = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=2)
    name_of_company = models.CharField(max_length=256)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    title_of_training = models.CharField(max_length=256)
    from_date = models.DateField(("Dates (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Dates (To)"), default=date.today,auto_now=False, auto_now_add=False)
    outcome = models.TextField()

    def __str__(self):
        return self.name_of_faculty

    def get_absolute_url(self):
        return reverse('ind_inst_2',)

#3] Faculty Providing training to industry
# No	Name of Faculty	Name of Department	Name of Company 		*Sector	Title of Training	Dates	Outcome
class IndInst3(models.Model):
    name_of_faculty = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=2)
    name_of_company = models.CharField(max_length=256)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    title_of_training = models.CharField(max_length=256)
    from_date = models.DateField(("Dates (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Dates (To)"), default=date.today,auto_now=False, auto_now_add=False)
    outcome = models.TextField()

    def __str__(self):
        return self.name_of_faculty

    def get_absolute_url(self):
        return reverse('ind_inst_3',)

#4] Faculty on board of Industry
# Name of Faculty	Name of Department	Name of Company	Date of Appointment	Type of Board/council	Designation of Faculty		Meeting Date(if any)
#some error so new model name here only
class IndInst4Model(models.Model):
    name_of_faculty = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=2)
    name_of_company = models.CharField(max_length=256)
    date_of_appointment = models.DateField(default=date.today, auto_now=False, auto_now_add=False)
    type_of_board = models.CharField(("Type of Board/Council"), max_length=150) # whether foreign key or not and values
    designation_of_faculty = models.CharField(max_length=150) # whether foreign key or not
    meeting_date = models.DateField(("Meeting Date(if any)"),blank=True)

    def __str__(self):
        return self.name_of_faculty

    def get_absolute_url(self):
        return reverse('ind_inst_4',)

#5] Industrial people on various Boards/Committee of Institute or Department                                        
# Type of Board/council	Name of Industry Member		Designation  	Name of Company		Sector	Tenure
class IndInst5(models.Model):
    type_of_board = models.CharField(("Type of Board/Council"), max_length=150) # whether foreign key or not and values
    name_of_industry_member = models.CharField(max_length=150)
    designation = models.CharField(max_length=150) # Foreign Key?
    name_of_company = models.CharField(max_length=250)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    tenure = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_industry_member

    def get_absolute_url(self):
        return reverse('ind_inst_5',)

#6] Faculty patents leading to industry products
# Name of Faculty	Title of Invention	Patent Number	Date of Grant/File	Name of Company		Sector	Date of Adoption
class IndInst6(models.Model):
    name_of_faculty = models.CharField(max_length=150)
    title_of_invention = models.CharField(max_length=150)
    patent_no = models.CharField(max_length=150)
    date_of_grant = models.DateField(("Date of Grant/File"),default=date.today, auto_now=False, auto_now_add=False)
    name_of_company = models.CharField(max_length=256)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    date_of_adoption = models.DateField(default=date.today, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name_of_faculty

    def get_absolute_url(self):
        return reverse('ind_inst_6',)

#7] Sponsored Projects (Faculty only)
#Title of  Project 	Name(s) of coordinator		Name of Sponsoring company		Duration	Grant Received	Status of Project
class IndInst7(models.Model):
    title_of_project = models.CharField(max_length=150)
    name_of_coordinator = models.CharField(max_length=150)
    name_of_sponsoring_company = models.CharField(max_length=150)
    duration_from = models.DateField(("Duration(From)"), default=date.today, auto_now=False, auto_now_add=False)
    duration_to = models.DateField(("Duration(To)"), default=date.today, auto_now=False, auto_now_add=False)
    grant_received = models.CharField(max_length=150, choices=GRANT, default='No')
    status_of_project = models.CharField(max_length=150)

    def __str__(self):
        return self.title_of_project

    def get_absolute_url(self):
        return reverse('ind_inst_7',)

#8] Consultancy Projects/Advisory Services
# Name of Faculty	Name of Company/ organization		Title of Project		Revenue Generated 	Dates	Status of Project
class IndInst8(models.Model):
    name_of_faculty = models.CharField(max_length=150)
    name_of_company = models.CharField(("Name of Company/ organization"),max_length=256)
    title_of_project = models.CharField(max_length=150)
    revenue_generated = models.IntegerField()
    dates_from = models.DateField(("Dates (From)"), default=date.today, auto_now=False, auto_now_add=False)
    dates_to = models.DateField(("Dates (To)"), default=date.today, auto_now=False, auto_now_add=False)
    status_of_project = models.CharField(max_length=150)

    def __str__(self):
        return self.name_of_faculty

    def get_absolute_url(self):
        return reverse('ind_inst_8',)

# 9] MOU Information
# Name of Department	Name of Faculty Coordinator		Name of Company		Sector	Date of MOU	Purpose of MOU
class IndInst9(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    name_of_faculty_coordinator = models.CharField(max_length=150)
    name_of_company = models.CharField(("Name of Company/ organization"),max_length=256)
    sector = models.CharField(max_length=150, choices=SECTOR)
    date_of_MOU = models.DateField(default=date.today, auto_now=False, auto_now_add=False)
    purpose_of_MOU = models.TextField()

    def __str__(self):
        return (self.name_of_company)

    def get_absolute_url(self):
        return reverse('ind_inst_9',)



##________________________________________________________________________________________________________
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(max_length=10, choices=ROLE,default="non-teach",blank=True)
    dept = models.CharField(max_length=4, choices=DEPT_PEM,default="VIEW",blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
