import django_filters
import datetime
from django_filters import DateFilter

from .models import *
from department.forms import DateInput


class StudentResultFilter(django_filters.FilterSet):

    from_date = DateFilter(widget=DateInput,field_name='exam_Date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='exam_Date', lookup_expr='lte', label='To')

    class Meta:
        model = StudentResult
        fields = ['department','from_date','to_date']




#Department filters

class DeptEvent1Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = DeptEvent1
        fields = ['department','from_date','to_date']
        
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
        
class ResProject1Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')


    class Meta:
        model = ResProject1
        fields = ['department','from_date','to_date']
        
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
        model = StudentResult
        fields = ['department','from_appointment_date','to_appointment_date','from_meeting_date','to_meeting_date']
        
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
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = CurStudTrain3
        fields = ['department','from_date','to_date']
        
class CurStudVisit4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='from_date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='to_date', lookup_expr='lte', label='To')

    class Meta:
        model = CurStudVisit4
        fields = ['department','from_date','to_date']
        
class StudFac1Filter(django_filters.FilterSet):
    class Meta:
        model = StudFac1
        fields = ['department']
        
class StudFac3Filter(django_filters.FilterSet):
    class Meta:
        model = StudFac3
        fields = ['department']
        
class ExtraAct6Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date', lookup_expr='lte', label='To')

    class Meta:
        model = ExtraAct6
        fields = ['department','from_date','to_date']
        

#                                          Placement Filters        
class Place1Filter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(Place1Filter, self).__init__(*args, **kwargs)
        self.form.initial['year'] = datetime.datetime.now().year

    class Meta:
        model = Placement1
        fields = ['year']

class Placement4Filter(django_filters.FilterSet):
    from_date = DateFilter(widget=DateInput,field_name='date_of_selection', lookup_expr='gte', label='From')
    to_date = DateFilter(widget=DateInput,field_name='date_of_selection', lookup_expr='lte', label='To')

    class Meta:
        model = Placement4
        fields = ['department','from_date','to_date']


#                                            Placement Filters   
class Library1Filter(django_filters.FilterSet):

    class Meta:
        model = Library1
        fields = ['year','month']


class Library2Filter(django_filters.FilterSet):

    class Meta:
        model = Library2
        fields = ['year','month']
        
