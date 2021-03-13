import datetime

DEPARTMENTS = (
    ('Computer Science','Computer Science'),
    ('Electronics and Telecommunication','Electronics and Telecommunication'),
    ('Mechanical','Mechanical'),
    ('Civil','Civil'),
)
CLASS = (
    ('', 'Choose...'),
    ('SE','SE'),
    ('TE','TE'),
    ('BE','BE'),
)

EXAM_TYPES=(
    ('', 'Choose...'),
    ('MID SEM','MID SEM'),
    ('PRELIMS','PRELIMS'),
    ('END SEM','END SEM'),
)

COMP_SUB = (
    ('DBMS','DBMS'),
    ('TOC','TOC'),
    ('CN','CN'),
    ('SEMP','SEMP'),
    ('ISEE','ISEE'),
)

ENTC_SUB = (
    ('ENTC1','ENTC1'),
    ('ENTC2','ENTC2'),
    ('ENTC3','ENTC3'),
    ('ENTC4','ENTC4'),
    ('ENTC5','ENTC5'),
)

MECH_SUB = (
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
)

CIVIL_SUB = (
    ('C1','C1'),
    ('C2','C2'),
    ('C3','C3'),
    ('C4','C4'),
    ('C5','C5'),
)

ENG_SUB = (
    ('PHYSICS','PHYSICS'),
    ('MATHS','MATHS'),
    ('CHEMISTRY','CHEMISTRY'),
    ('ELECTRONICS','ELECTRONICS'),
    ('ELECTRICAL','ELECTRICAL'),
    ('GRAPHICS','GRAPHICS'),
    ('MECHANICS','MECHANICS'),
)

SUBJECTS =(
    ('', 'Choose...'),
    ('COMPUTER SUBJECTS',COMP_SUB),
    ('ENTC SUBJECTS',ENTC_SUB),
    ('MECHANICAL SUBJECTS',MECH_SUB),
    ('CIVIL SUBJECTS',CIVIL_SUB),
    ('ENGINEERING SCIENCE SUBJECTS',ENG_SUB),
)

GRANT = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

SECTOR = [
    ('Agriculture','Agriculture'),
    ('Banking','Banking'),
    ('Construction','Construction'),
    ('Consumer durables','Consumer durables'),
    ('Engineering','Engineering'),
    ('Health care','Health care'),
    ('IT','IT'),
    ('Metal and mining','Metal and mining'),
    ('Oil and Gas','Oil and Gas'),
    ('Power','Power'),
    ('Retail','Retail'),
    ('Service','Service'),
    ('Transport','Transport'),
    ('others','others')
]

COMPETITIVE_EXAM = (
    ('', 'Choose...'),
    ("MPSC","MPSC"),
    ("UPSC","UPSC"),
    ("GATE","GATE"),
    ("GRE","GRE"),
    ("IELTS","IELTS"),
    ("TOEFL","TOEFL"),
    ("CAT","CAT"),
    ("Others","Others"),
)

SELF_LEARNING = (
    ('', 'Choose...'),
    ("Webinars", "Webinars"),
    ("Podcast", "Podcast"),
    ("MOOC’s", "MOOC’s"),
    ("NPTEL courses", "NPTEL courses"),
    ("Myexamo", "Myexamo"),
    ("Others", "Others"),
)

ACTIVITY = (
    ('', 'Choose...'),
    ("Soft Skill Development", "Soft Skill Development"), 
    ("Remedial Coaching", "Remedial Coaching"), 
    ("Language Lab", "Language Lab"),
    ("Yoga", "Yoga"), 
    ("Meditation", "Meditation"), 
    ("Personal Counseling", "Personal Counseling"), 
    ("Bridge Courses", "Bridge Courses"), 
    ("Competitive Examination", "Competitive Examination"), 
    ("Higher", "Higher"),
)

APPROVAL=(
    ('', 'Choose...'),
    ('UGC','UGC'),
    ('SCOPUS','SCOPUS'),
    ('Web of Science','Web of Science'),
    ('Other','Other'),
)

#Library2.Details choices
DETAILS =(
    ('', 'Choose...'),
    ('Number of Faculties Visited','Number of Faculties Visited'),
    ('Number of Students Visited','Number of Students Visited'),
    ('Number of Faculty Transctions','Number of Faculty Transctions'),
    ('Number of Student Transactions','Number of Student Transactions'),
)

# Year Dropdown choice designed for Placement table queries
YEAR_CHOICES = []
for r in range(2008, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

MONTH_CHOICES=(
    ('January','January'),
    ('February','February'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December'),
    )


ROLE=(
    ('admin','admin'),
    ('HOD','HOD'),
    ('sadmin','sadmin'),
    ('teacher','teacher'),
    ('non-teach','non-teach')
    )
    
DEPT_ROLE = (
    ('Non-Teaching','Non-Teaching'),
    ('Computer Science','Computer Science'),
    ('Electronics and Telecommunication','Electronics and Telecommunication'),
    ('Mechanical','Mechanical'),
    ('Civil','Civil'),
    ('Other','Other')
)

DEPT_PEM=(
    ('ALLD','ALLD'),
    ('COMP','COMP'),
    ('ENTC','ENTC'),
    ('MECH','MECH'),
    ('CIVI','CIVI'),
    ('VIEW','VIEW')
    )
