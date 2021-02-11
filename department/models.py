from django.db import models
from datetime import date
from .choices import *
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator # used on line 912

# Questionable fields
# level, student_ID_number

# Create your models here.

# Models with Primary Keys
## remaining --designation,
class Department(models.Model):
    department = models.CharField(("Department Name"),primary_key=True, max_length=128,unique=True)

    def __str__(self):
        return self.department

#-------------------------------------------------------------------------------------
                        # STUDENTS ACADEMIC PERFORMANCE
                        
# Students Result in various examinations during specified period 
class StudentResult(models.Model):
    # department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Class = models.CharField(max_length = 150, choices=CLASS, default='')
    exam_Type = models.CharField(max_length = 150, choices=EXAM_TYPES, default='')
    subject = models.CharField(max_length = 150, choices=SUBJECTS, default='')
    exam_Date = models.DateField(("Exam Date"), default=date.today,auto_now=False, auto_now_add=False)
    appeared = models.IntegerField(null=False, blank=False)
    passed = models.IntegerField(null=False, blank=False)
    percentage = models.DecimalField(("Percentage"), default=0 ,decimal_places=2 , max_digits=10)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.percentage = (self.passed / self.appeared)* 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('stud_result',)
    



#-------------------------------------------------------------------------------------
                          # DEPARTMENTAL ACTIVITIES

#1] Information about events organized by department
class DeptEvent1(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    event_type = models.CharField(("Event Type"),max_length=150)
    event_name = models.CharField(("Event Name"),max_length=150)
    guest_name = models.CharField(("Guest Name"),max_length=150)
    guest_Affiliation = models.CharField(("Affiliation of guest"),max_length=250)
    no_of_Participants = models.IntegerField(("No of Participants"))
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('dept_act_1',)

#2] Information about events organized by department (For nearby schools only)
class DeptEvent2(models.Model):
    activity_name = models.CharField(("Activity Name"),max_length=150)
    school = models.CharField(max_length=150)
    school_Contact = models.CharField(("School Contact Details"),max_length=250)
    faculty_name = models.CharField(("Faculty Name"),max_length=250)
    no_of_Participants = models.IntegerField(("No of Participants"))
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.activity_name

    def get_absolute_url(self):
        return reverse('dept_act_2',)

#3] Information about events organized by department in association with Professional bodies
class DeptProEvent3(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    activity = models.CharField(max_length=150)
    resourse_person = models.CharField(max_length=150)
    resourse_person_contact = models.IntegerField()
    no_of_Participants = models.IntegerField(("No of Participants"))
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    objects = models.Manager()

    def __str__(self):
        return self.activity
 
    def get_absolute_url(self):
        return reverse('dept_act_3',)

#4] Information about Faculty Development Programs organized by department 
class DeptFacultyDev4(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    program = models.CharField(max_length=150)
    agency = models.CharField(max_length=150)
    amount_Sponsored = models.IntegerField(default=0)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_Participants = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)

    def __str__(self):
        return self.program

    def get_absolute_url(self):
        return reverse('dept_act_4',)

#5] Participation in inter-institute events by students 
class DeptStudPart5(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    student_name = models.CharField(max_length=150)
    event_type = models.CharField(max_length=150)
    event_name = models.CharField(max_length=150)
    organising_Institute = models.CharField(max_length=264)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_Participants = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)
    awards = models.CharField(("Recognition Awards"), max_length=264)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('dept_act_5',)

#6] Start-Up
class DeptStartUp6(models.Model):
    startup_name = models.CharField(max_length=150)
    startup_nature = models.CharField(max_length=150)
    start_date = models.CharField(("Commencement Date"),max_length=150)
    founder = models.CharField(max_length=150)
    LLP_number = models.IntegerField(("LLP number"))
    website = models.URLField(max_length=150)
    team_members = models.CharField(max_length=500)

    def __str__(self):
        return self.startup_name

    def get_absolute_url(self):
        return reverse('dept_act_6',)


#-------------------------------------------------------------------------------------
                            # FACULTY CONTRIBUTION

#1] Research projects in the specified period
class ResProject1(models.Model):
    title = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=150)
    date = models.DateField(default=date.today,auto_now=False, auto_now_add=False)
    agency = models.CharField(max_length=150)
    other = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fac_contri_1',)


#2] Funds received for research for projects mentioned above
class ResFunds2(models.Model):
    funding_agency = models.CharField(max_length=150)
    grants_recieved = models.IntegerField(default=0)
    grants_utilized = models.IntegerField(default=0)
    remaining_grant = models.IntegerField(default=0)

    def __str__(self):
        return self.funding_agency

    def get_absolute_url(self):
        return reverse('fac_contri_2',)


#3] Research papers published in International journals in the specified period
class ResInternational3(models.Model):
    title = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    authors_name = models.CharField(max_length=150)
    journal_name = models.CharField(max_length=150)
    date_of_publication = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    volume_Issue_ICV = models.CharField(("Volume, Issue, Page Number and Impact Factor/ICV"), max_length=150)
    amount = models.IntegerField(("Amount (if paid by institute)"), default=0)
    approval = models.CharField(max_length=150, choices=APPROVAL, default='')
    url = models.URLField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fac_contri_3',)


#4] Research papers published in national journals in the specified period
class ResNational4(models.Model):
    title = models.CharField(("Title of the paper"), max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    authors_name = models.CharField(max_length=150)
    journal_name = models.CharField(max_length=150)
    date_of_Publication = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    volume_Issue_ICV = models.CharField(("Volume, Issue, Page Number and Impact Factor/ICV"), max_length=150)
    amount = models.IntegerField(("Amount (if paid by institute)"), default=0)
    approval = models.CharField(max_length=150, choices=APPROVAL, default='')
    url = models.URLField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fac_contri_4',)

#5] Paper presented in International Conferences in the specified period
class ConfInternational5(models.Model):
    title = models.CharField(("Title of the paper"), max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    authors_Name = models.CharField(max_length=150, null=True)
    conference_Name = models.CharField(max_length=150, null=True)
    oraganised_by = models.CharField(max_length=150, null=True)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    amount = models.IntegerField(("Amount (if paid by institute)"), default=0)
    location = models.CharField(max_length=150, null=True)
    url = models.URLField(max_length=150, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fac_contri_5',)


#6] Paper presented in National Conferences in the specified period
class ConfNational6(models.Model):
    title = models.CharField(("Title of the paper"), max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    authors_Name = models.CharField(max_length=150)
    conference_Name = models.CharField(max_length=150)
    oraganised_by = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    amount = models.IntegerField(("Amount (if paid by institute)"), default=0)
    location = models.CharField(max_length=150)
    url = models.URLField(max_length=150, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fac_contri_6',)


#7] Research papers authored with industrial persons
class ResIndustrial7(models.Model):
    title = models.CharField(("Title of the paper"), max_length=150)
    authors_Name = models.CharField(max_length=150)
    co_Author_Name = models.CharField(max_length=150)
    name_of_Company = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    name_of_Conference_or_Journal = models.CharField(('Name of Conference/Details of Journal'),max_length=150) #tweak
    location = models.CharField(max_length=150)
    url = models.URLField(max_length=150, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fac_contri_7',)

#8] Events for faculty members (FDP/Webinar/Seminar/STTP/Workshops/Others)
class FacEvents8(models.Model):
    event_Type = models.CharField(max_length=150)
    event_Name = models.CharField(max_length=150)
    name_of_Faculty = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    level = models.CharField(max_length=150)
    amount = models.IntegerField(default=0)
    organising_Institute = models.CharField(max_length=150)

    def __str__(self):
        return self.event_Type

    def get_absolute_url(self):
        return reverse('fac_contri_8',)


#9] Participation in Professional Practices (Curriculum Revision/Syllabus Development/Others)
class ProfessionalPrac9(models.Model):
    faculty_Name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    professional_Practice_Type = models.CharField(('Type of professional practices'),max_length=150)
    designation = models.CharField(('Designation in Professional Practices'),max_length=150)
    organising_Institute = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.faculty_Name

    def get_absolute_url(self):
        return reverse('fac_contri_9',)


#10] List of Faculty Patents/IPR
class FacPatents10(models.Model):
    faculty_Name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    invention_Title = models.CharField(('Title of Invention'),max_length=150)
    patent_Number = models.IntegerField(('Patent/Application Number'))
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    patent_Status = models.CharField(("Current Status of Patent"), max_length=150)

    def __str__(self):
        return self.faculty_Name

    def get_absolute_url(self):
        return reverse('fac_contri_10',)


#11] Details of National Conference attended
class NationalAttend11(models.Model):
    faculty_Name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    conference_Name = models.CharField(('Name of the Conference'),max_length=150)
    organised_By = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    amount = models.IntegerField(('Amount (if paid by institute)'), default=0)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.faculty_Name

    def get_absolute_url(self):
        return reverse('fac_contri_11',)

#12] Details of International Conference attended
class InternationalAttend12(models.Model):
    faculty_Name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    conference_Name = models.CharField(('Name of the Conference'),max_length=150)
    organised_By = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    amount = models.IntegerField(('Amount (if paid by institute)'), default=0)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.faculty_Name

    def get_absolute_url(self):
        return reverse('fac_contri_12',)


#-------------------------------------------------------------------------------------
                            # FACULTY ACHIEVEMENTS

#1] Achievement List
class FacAchieve(models.Model):
    faculty_Name = models.CharField(("Faculty Name"), max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    achievement = models.CharField(max_length=150)
    level = models.CharField(max_length=150)
    dates = models.DateField(("Dates"), default=date.today,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.faculty_Name

    def get_absolute_url(self):
        return reverse('fac_achieve',)


#2] Names of books/Chapters/Manuals/ Monographs published
class FacBook(models.Model):
    title = models.CharField(("Title"),max_length=500)
    author_name = models.CharField(("Name of author(s)"),max_length=150)
    publication = models.CharField(("Publication"),max_length=150)
    ISBN = models.IntegerField(("ISBN number"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fac_book',)


#-------------------------------------------------------------------------------------
                            #INDUSTRY – INSTITUTE INTERACTION

#1] Industrial Visit  of Faculty (Visits accompanied with students should be excluded)
class IndFacvisit1(models.Model):
    faculty = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.CharField(("Name of Company"), max_length=256)
    sector = models.CharField(choices=SECTOR, max_length=150)
    purpose = models.TextField(("Purpose of Visit"), max_length=256)
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
    sector = models.CharField(choices=SECTOR, max_length=150)
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
    sector = models.CharField(choices=SECTOR, max_length=150)
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
class IndInst4(models.Model):
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
    sector = models.CharField(choices=SECTOR, max_length=150)
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
    sector = models.CharField(choices=SECTOR, max_length=150)
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


#-------------------------------------------------------------------------------------
                          # CURRICULUM INPUT
                          
#1] Guest Lectures (General Topics)
class CurGuestLect1(models.Model):
    guest = models.CharField(("Name of Guest"),max_length = 150)
    organization = models.CharField(("Company/Organization Represented"),max_length=150)
    designation = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_Participants = models.IntegerField(("No of Participants"))

    def __str__(self):
        return self.guest

    def get_absolute_url(self):
        return reverse('cur_input_1',)


#2] Expert Lectures (Subject-Specific Topics)
class CurExptLect2(models.Model):
    guest = models.CharField(("Name of Guest"),max_length = 150)
    organization = models.CharField(("Company/Organization Represented"),max_length=150)
    designation = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_Participants = models.IntegerField(("No of Participants"))

    def __str__(self):
        return self.guest

    def get_absolute_url(self):
        return reverse('cur_input_2',)

# class ExptLect2(GuestLect1):
#     pass
  
#3] Student Internship/Industrial training
    # No	Name of Department	Name of Student		Name of Company		Sector		Date/Duration
class CurStudTrain3(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    student_name = models.CharField(("Name of Student"), max_length=150)
    company = models.CharField(("Name of Company"), max_length=250)
    sector = models.CharField(max_length=250)
    from_date = models.DateField(("Duration (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Duration (To)"), default=date.today,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('cur_input_3',)

#4] Student Industrial Visit
class CurStudVisit4(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    company = models.CharField(("Name of Company"), max_length=250)
    sector = models.CharField(max_length=250)
    faculty_Name = models.CharField(("Faculty Name"),max_length=150)
    no_of_Students = models.IntegerField(("No of Students"))
    from_date = models.DateField(("Duration (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Duration (To)"), default=date.today,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('cur_input_4',)

#5] Student Sponsored Projects
class CurStudSponsor5(models.Model):
    title = models.CharField(("Title of Project"),max_length=250)
    company_Representative = models.CharField(("Name of Company Representative"), max_length=250)
    sponsoring_Company = models.CharField(("Name of Sponsoring company"), max_length=250)
    from_date = models.DateField(("Duration (From)"), default=date.today, auto_now=False, auto_now_add=False)
    to_date = models.DateField(("Duration (To)"), default=date.today,auto_now=False, auto_now_add=False)
    grant = models.CharField(("Grant Received"), max_length=150, choices=GRANT, default='No')
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cur_input_5',)

# class MY_CHOICES(models.Model)
#     choice = models.CharField(max_length=154, unique=True)

# class MODEL(models.Model):
#     ...
#     ...
#     my_field = models.ManyToManyField(MY_CHOICES)
    

#-------------------------------------------------------------------------------------
                            #STUDENT /FACULTY SUPPORT SYSTEM

#1] Mentoring System to help students at individual level
#Name of Department	Class/ Division	Type of Meeting (GFM/HOD)	Name of Faculty 		*Type of Mentoring		Dates of mentoring activity
class StudFac1(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    class_or_division = models.CharField(max_length=150)
    type_of_meeting_open_GFM_or_HOD_close = models.CharField(("Type of meeting (GFM/HOD)"), max_length=150)
    name_of_faculty = models.CharField(max_length=150)
    type_of_mentoring = models.CharField(max_length=150)
    dates_of_mentoring_activity = models.CharField(max_length=150)

    def __str__(self):
        return self.class_or_division

    def get_absolute_url(self):
        return reverse('stud_fac_1',)

#2]Self Learning facilities for students
# Class / Division	Type of Self Learning Facility		Name of Subject		No of students participated	Dates 	Certificate/Award Received by students if any
class StudFac2(models.Model):
    class_or_division = models.CharField(max_length=150)
    type_of_self_learning_facility = models.CharField(max_length=150, choices=SELF_LEARNING, default=1)
    name_of_subject = models.CharField(max_length=150)
    no_of_student_participated = models.PositiveIntegerField()
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    certificate_or_award_received_by_students = models.CharField(("Certificate/Award Received by students (if any)"),max_length=150, blank=True)

    def __str__(self):
        return self.class_or_division

    def get_absolute_url(self):
        return reverse('stud_fac_2',)

#3]Achievement of Students in Competitive Exam 
# Name of Student		Name of Department		*Name of Competitive exam appeared/qualified 		Competitive Exam Seat No.	Score
class StudFac3(models.Model):
    name_of_student = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    name_of_competitive_exam_appeard_or_qualified = models.CharField(max_length=150, choices=COMPETITIVE_EXAM, default=1)
    competitive_exam_seat_no = models.CharField(max_length=150)
    score = models.FloatField()

    def __str__(self):
        return self.name_of_student

    def get_absolute_url(self):
        return reverse('stud_fac_3',)

#4]Capability Enhancement and Development Activities
# Name of Activity*			Date of implementation		Number of Students Enrolled		Agencies involved
class StudFac4(models.Model):
    name_of_activity = models.CharField(max_length=150, choices=ACTIVITY, default=1)
    date_of_implementation = models.DateField(default=date.today, auto_now=False, auto_now_add=False)
    no_of_students_enrolled = models.PositiveIntegerField()
    agencies_involved = models.CharField(max_length=250)

    def __str__(self):
        return self.name_of_activity

    def get_absolute_url(self):
        return reverse('stud_fac_4',)

#5]Number of professional development / administrative training  programmes organized
# Title of the professional development program* 		Organized for Faculty / Staff	Organizing Department 		Duration (from-to)	No. of participants	Agencies involved
class StudFac5(models.Model):
    title_of_the_professional_development_program = models.CharField(max_length=150)
    organized_for_faculty_or_staff = models.CharField(("Organized for Faculty/Staff"), max_length=150)
    organizing_department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    duration_open_from_close = models.DateField(("Duration (From)"),default=date.today, auto_now=False, auto_now_add=False)
    duration_open_to_close = models.DateField(("Duration (To)"),default=date.today, auto_now=False, auto_now_add=False)
    no_of_Participants = models.PositiveIntegerField()
    agencies_involved = models.CharField(max_length=250)

    def __str__(self):
        return self.title_of_the_professional_development_program

    def get_absolute_url(self):
        return reverse('stud_fac_5',)

#-------------------------------------------------------------------------------------
                                #EXTRA CURRICULAR ACTIVITIES

#1] Sports (This information to be provided by Physical/Sports Director)
# Activity	Organized by			Level		Date	Number of Students Participated
class ExtraCurr1(models.Model):
    activity = models.CharField(max_length=150)
    organized_by = models.CharField(max_length=150)
    level = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_Students_Participated = models.PositiveIntegerField()

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('extra_curr_1',)

#2] Names of winners at various levels of  sports tournaments
# Name of the Sport / Team	Name of the student		Student ID Number	Name of Department		Level	Rank
# *A detailed descriptive report with photographs by Sports Director
class ExtraCurr2(models.Model):
    name_of_the_sport_or_team = models.CharField(("Name of the Sport / Team"), max_length=250)
    student_ID_number = models.CharField(max_length=100)
    name_of_department = models.ForeignKey(Department, default=1, on_delete=models.CASCADE)
    level = models.CharField(max_length=100)
    rank = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.student_ID_number

    def get_absolute_url(self):
        return reverse('extra_curr_2',)

# CULTURAL ACTIVITIES
#3] Number of students participated in cultural competitions other than institute level
class CulturalCount3(models.Model):
    no_of_events = models.PositiveIntegerField(default=12)
    solo_Performances = models.PositiveIntegerField(default=10)
    team_Performances = models.PositiveIntegerField(default=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.no_of_events

    def get_absolute_url(self):
        return reverse('extra_curr_3',)


     
#3] Awards won in cultural competitions/Club activities
class CulturalAct3(models.Model,):
    event_Name = models.CharField(max_length=150)
    organized_By = models.CharField(max_length=150)
    level = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    Prize_Won_or_Medal = models.CharField(("Prize Won/ Medal"), max_length=150)
    no_of_Students_Participated = models.PositiveIntegerField()

    def __str__(self):
        return self.event_Name

    def get_absolute_url(self):
        return reverse('extra_curr_3',)

# SOCIAL ACTIVITIES
#4] Information about social activities held in the specified period
class SocialAct4(models.Model):
    activity_Name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    no_of_Faculties_Participated = models.CharField(("No. of Faculties Participated"), max_length=150)
    no_of_Students_Participated = models.CharField(("No. of Students Participated"), max_length=150)
    no_of_People_Benefited = models.CharField(("No. of people benefited"), max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    Awards_or_Recognition_open_if_any_close = models.CharField(("Awards/Recognition (if any)"), max_length=150)

    def __str__(self):
        return self.activity_Name

    def get_absolute_url(self):
        return reverse('extra_curr_4',)

#5] Activities of Various Centers/Cells (ISTE/Research/Skill Development Center etc)
class CentersAct5(models.Model):
    Center_or_Cell = models.CharField(("Name of Center/Cell"), max_length=150)
    Program_or_Activity = models.CharField(("Name of Program/Activity"), max_length=150)
    sponsoring_Agency = models.CharField(max_length=150)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    level = models.CharField(max_length=150)
    no_of_Participants = models.PositiveIntegerField()

    def __str__(self):
        return self.Center_or_Cell

    def get_absolute_url(self):
        return reverse('extra_curr_5',)

#6] Extra Activities/Acheivement(if any)
class ExtraAct6(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=150)
    activity = models.CharField(max_length=256)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    achievement = models.CharField(max_length=150)

    def __str__(self):
        return self.faculty

    def get_absolute_url(self):
        return reverse('extra_curr_6',)


#-------------------------------------------------------------------------------------
                                    #E - CELL

#1] Activities Conducted By E- Cell
class Ecell(models.Model):
    activity = models.CharField(max_length=250)
    organised_By = models.CharField(max_length=150)
    level = models.CharField(max_length=100)
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_Students_Participated = models.PositiveIntegerField()

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('e_cell',)

#1] Numerical information about various activities in the specified period
class EcellCount(models.Model):
    activity_Name =  models.CharField(max_length=250)
    civil = models.PositiveIntegerField(default=1)
    computer = models.PositiveIntegerField(default=10)
    E_andTC = models.PositiveIntegerField(default=10)
    mechanical = models.PositiveIntegerField(default=10)
    first_Year = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.activity_Name

    def get_absolute_url(self):
        return reverse('e_cell',)

def save(self, *args, **kwargs):
 if EcellCount.objects.count() != 6:    
    EcellCount.objects.create(activity_Name="Number of Research paper in UGC Approved Journal",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1)
    EcellCount.objects.create(activity_Name="Number of Patent Filed/Published",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1)
    EcellCount.objects.create(activity_Name="NUmber of Activities Conducted By E- Cell",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1)
    EcellCount.objects.create(activity_Name="Number of International Conference attended",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1)
    EcellCount.objects.create(activity_Name="Number of NationalConference attended",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1)
    EcellCount.objects.create(activity_Name="Number of Start-Ups",civil=1, computer=1, E_andTC=1, mechanical=1, first_Year=1)
    super(EcellCount, self).save(*args, **kwargs)
 else : pass


# one_entry = Entry.objects.get(pk=1)


#-------------------------------------------------------------------------------------------------------------------
                                        #PLACEMENT

#1] Numerical information about placement  
class Placement1(models.Model):
    year = models.IntegerField(('year'),unique=True, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    companies_Visited = models.PositiveIntegerField(('Number of Companies visited for Campus Recruitment'))
    students_Placed = models.PositiveIntegerField(('Number of Students Placed'))
    students_Placed_Percentage = models.PositiveIntegerField(('Percentage of students placed'))
    max_Salary = models.PositiveIntegerField(('Maximum Salary offered (p.a.)'), default=100000
                                                , validators=[MinValueValidator(100000), MaxValueValidator(10000000)])
    min_Salary = models.PositiveIntegerField(('Minimum Salary offered (p.a.)'), default=100000
                                                , validators=[MinValueValidator(100000), MaxValueValidator(10000000)])
    average_Salary = models.PositiveIntegerField(('Average of salary offered (p.a.)'), default=100000
                                                , validators=[MinValueValidator(100000), MaxValueValidator(10000000)])

    def __str__(self):
        return str(self.year)

    def get_absolute_url(self):
        return reverse('place1',)

#2] List of companies visited  for campus placement in specified period								
# No.	Name of company		Sector	Discipline	Dates of Drive	No of eligible students 	No of  students offered jobs	Package
class Placement2(models.Model):
    name_of_company = models.CharField(max_length=150)
    sector = models.CharField(max_length=150)
    discipline = models.CharField(max_length=150)
    dates_of_drive = models.CharField(max_length=150)
    no_of_eligible_students = models.PositiveIntegerField()
    no_of_students_offered_jobs = models.PositiveIntegerField()
    package = models.PositiveIntegerField()

    def __str__(self):
        return self.name_of_company

    def get_absolute_url(self):
        return reverse('place2',)

#3] List of companies for which students appeared at other campus in specified period								
#No.	Name of company		Sector	Location (College/Industry)	Date of Walk-in	No. of students appeared	No. of students offered job	Package
class Placement3(models.Model):
    name_of_company = models.CharField(max_length=150)
    sector = models.CharField(max_length=150)
    location_open_College_or_Industry_close = models.CharField(max_length=200)
    date_of_walk_in = models.DateField(("Date of Walk-In"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_students_appeared = models.PositiveIntegerField()
    no_of_students_offered_jobs = models.PositiveIntegerField()
    package = models.PositiveIntegerField()

    def __str__(self):
        return self.name_of_company

    def get_absolute_url(self):
        return reverse('place3',)

#Student Placement Data								
#No	Name of Student placed		Department	Name of Employer		Date of Selection	Package	Appointment reference No
class Placement4(models.Model):
    name_of_student = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name_of_employer = models.CharField(max_length=150)
    date_of_selection = models.DateField(("Date of Selection"), default=date.today,auto_now=False, auto_now_add=False)
    package = models.PositiveIntegerField()
    appointment_reference_no = models.CharField(max_length=150)

    def __str__(self):
        return self.name_of_student

    def get_absolute_url(self):
        return reverse('place4',)

#4] List of Students Opted for Entrepreneurship/Self Employment   (During specified period)								
#No	Name of Student		Discipline	Type of Self Employment (Start up /NGO)		Name of Firm/Company		Products /Services offered
class Placement5(models.Model):
    name_of_student = models.CharField(max_length=150)
    discipline = models.CharField(max_length=150)
    type_of_self_employment = models.CharField(choices=(("Start up", "Start up"), ("NGO", "NGO")), max_length=150)
    name_of_firm_or_company = models.CharField("Name of Firm/ Company", max_length=150)
    products_or_services_offered = models.CharField("Products/ Services offered", max_length=150)

    def __str__(self):
        return self.name_of_student

    def get_absolute_url(self):
        return reverse('place5',)

##__________________________________________________________________________________________________
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(max_length=10, choices=ROLE, default="non-teach",blank=True)
    dept = models.CharField(max_length=4, choices=DEPT_PEM, default="VIEW",blank=True)

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
