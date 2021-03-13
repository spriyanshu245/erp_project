import django_filters
import datetime
from django_filters import *

from .models import *
from department.forms import DateInput


class StudentResultFilter(django_filters.FilterSet):

    from_date = DateFilter(widget=DateInput,field_name='exam_Date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='exam_Date', lookup_expr='lte', label='To')
    class Meta:
        model = StudentResult
        fields = ['department','from_date','to_date','created_by']


#Department filters

class DeptEvent1Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = DeptEvent1
        fields = ['department','from_date','to_date']

class DeptEvent2Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = DeptEvent2
        fields = ['from_date','to_date']
        
class DeptProEvent3Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = DeptProEvent3
        fields = ['department','from_date','to_date']
        
class DeptFacultyDev4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = DeptFacultyDev4
        fields = ['department','from_date','to_date']
        
class DeptStudPart5Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = DeptStudPart5
        fields = ['department','from_date','to_date']

class DeptStartUp6Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='start_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='start_date', lookup_expr='lte', label='To')

    class Meta:
        model = DeptStartUp6
        fields = ['from_date','to_date']
        
class ResProject1Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ResProject1
        fields = ['department','from_date','to_date']

class ResFunds2Filter(django_filters.FilterSet):

    class Meta:
        model = ResFunds2
        fields = ['created_by']

class ResInternational3Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date_of_publication', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date_of_publication', lookup_expr='lte', label='To')

    class Meta:
        model = ResInternational3
        fields = ['department', 'from_date', 'to_date']
        
class ResNational4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date_of_Publication', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date_of_Publication', lookup_expr='lte', label='To')

    class Meta:
        model = ResNational4
        fields = ['department','from_date','to_date']
        
class ConfInternational5Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ConfInternational5
        fields = ['department','from_date','to_date']
        
class ConfNational6Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ConfNational6
        fields = ['department','from_date','to_date']

class ResIndustrial7Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ResIndustrial7
        fields = ['from_date','to_date','created_by']

class FacEvents8Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = FacEvents8
        fields = ['department','from_date','to_date']
        
class ProfessionalPrac9Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ProfessionalPrac9
        fields = ['department','from_date','to_date']
        
class FacPatents10Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = FacPatents10
        fields = ['department','from_date','to_date']
        
class NationalAttend11Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = NationalAttend11
        fields = ['department','from_date','to_date']
        
class InternationalAttend12Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = InternationalAttend12
        fields = ['department','from_date','to_date']
        
class FacAchieveFilter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='dates', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='dates', lookup_expr='lte', label='To')

    class Meta:
        model = FacAchieve
        fields = ['department','from_date','to_date']

class FacBookFilter(django_filters.FilterSet):
    
    class Meta:
        model = FacBook
        fields = ['created_by']

class IndFacvisit1Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = IndFacvisit1
        fields = ['department','from_date','to_date']
        
class IndInst2Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = IndInst2
        fields = ['department','from_date','to_date']
        
class IndInst3Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = IndInst3
        fields = ['department','from_date','to_date']
        
class IndInst4Filter(django_filters.FilterSet):
    from_appointment_date = DateFilter(widget=DateInput,field_name='date_of_appointment', lookup_expr='gte', label='From')
    to_appointment_date = DateFilter(widget=DateInput,field_name='date_of_appointment', lookup_expr='lte', label='To')
    from_meeting_date = DateFilter(widget=DateInput,field_name='meeting_date', lookup_expr='gte', label='From')
    to_meeting_date = DateFilter(widget=DateInput,field_name='meeting_date', lookup_expr='lte', label='To')

    class Meta:
        model = IndInst4
        fields = ['department','from_appointment_date','to_appointment_date','from_meeting_date','to_meeting_date']

class IndInst5Filter(django_filters.FilterSet):
    
    class Meta:
        model = IndInst5
        fields = ['sector','created_by']

class IndInst6Filter(django_filters.FilterSet):
    adoption_from_date = DateFilter(widget=DateInput,field_name='date_of_adoption', lookup_expr='gte', label='From')
    adoption_to_date = DateFilter(widget=DateInput,field_name='date_of_adoption', lookup_expr='lte', label='To')
    grant_from_date = DateFilter(widget=DateInput,field_name='date_of_grant', lookup_expr='gte', label='From')
    grant_to_date = DateFilter(widget=DateInput,field_name='date_of_grant', lookup_expr='lte', label='To')

    class Meta:
        model = IndInst6
        fields = ['grant_from_date','grant_to_date',
            'adoption_from_date','adoption_to_date',
            'sector','created_by']

class IndInst7Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='duration_from', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='duration_to', lookup_expr='lte', label='To')

    class Meta:
        model = IndInst7
        fields = ['from_date','to_date','created_by']

class IndInst8Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='dates_from', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='dates_to', lookup_expr='lte', label='To')

    class Meta:
        model = IndInst8
        fields = ['from_date','to_date','created_by']

class IndInst9Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date_of_MOU', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date_of_MOU', lookup_expr='lte', label='To')

    class Meta:
        model = IndInst9
        fields = ['department','from_date','to_date']
        
class CurGuestLect1Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = CurGuestLect1
        fields = ['department','from_date','to_date']
        
class CurExptLect2Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = CurExptLect2
        fields = ['department','from_date','from_date']
        
class CurStudTrain3Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='lte', label='To')

    class Meta:
        model = CurStudTrain3
        fields = ['department','from_date','to_date']
        
class CurStudVisit4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = CurStudVisit4
        fields = ['department','from_date','to_date']

class CurStudSponsor5Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = CurStudSponsor5
        fields = ['from_date','to_date','created_by']

class StudFac1Filter(django_filters.FilterSet):
    class Meta:
        model = StudFac1
        fields = ['department']

class StudFac2Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = StudFac2
        fields = ['from_date','to_date','created_by']
        
class StudFac3Filter(django_filters.FilterSet):
    class Meta:
        model = StudFac3
        fields = ['department']

class StudFac4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date_of_implementation', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date_of_implementation', lookup_expr='lte', label='To')

    class Meta:
        model = StudFac4
        fields = ['from_date','to_date','created_by']

class StudFac5Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='duration_open_from_close', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='duration_open_to_close', lookup_expr='lte', label='To')

    class Meta:
        model = StudFac5
        fields = ['from_date','to_date','created_by']

class ExtraCurr1Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ExtraCurr1
        fields = ['from_date','to_date','created_by']

class ExtraCurr2Filter(django_filters.FilterSet):
    
    class Meta:
        model = ExtraCurr2
        fields = ['department','created_by']

class CulturalCount3Filter(django_filters.FilterSet):

    class Meta:
        model = CulturalCount3
        fields = ['created_by']

class CulturalAct3Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = StudFac5
        fields = ['from_date','to_date','created_by']

class SocialAct4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = SocialAct4
        fields = ['from_date','to_date','created_by']

class CenterAct5Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = CentersAct5
        fields = ['from_date','to_date','created_by']

class ExtraAct6Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ExtraAct6
        fields = ['department','from_date','to_date']
        
class StudFac5Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='duration_open_from_close', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='duration_open_to_close', lookup_expr='lte', label='To')

    class Meta:
        model = StudFac5
        fields = ['from_date','to_date','created_by']

#Ecell

#                                          Placement Filters
   
class Place1Filter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(Place1Filter, self).__init__(*args, **kwargs)
        self.form.initial['year'] = datetime.datetime.now().year

    class Meta:
        model = Placement1
        fields = ['year']

#Placement2Filter

class Placement3Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date_of_walk_in', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date_of_walk_in', lookup_expr='lte', label='To')

    class Meta:
        model = Placement3
        fields = ['from_date','to_date','sector','created_by']

class Placement4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date_of_selection', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date_of_selection', lookup_expr='lte', label='To')

    class Meta:
        model = Placement4
        fields = ['department','from_date','to_date']

class Placement5Filter(django_filters.FilterSet):
    
    class Meta:
        model = Placement5
        fields = ['created_by']


#                                            Library Filters   
class Library1Filter(django_filters.FilterSet):

    class Meta:
        model = Library1
        fields = ['year','month','created_by']


class Library2Filter(django_filters.FilterSet):

    class Meta:
        model = Library2
        fields = ['year','month','created_by']
        
