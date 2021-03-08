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
        fields = ['from_date','to_date']


class Place1Filter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(Place1Filter, self).__init__(*args, **kwargs)
        self.form.initial['year'] = datetime.datetime.now().year

    class Meta:
        model = Placement1
        fields = ['year']



class Library1Filter(django_filters.FilterSet):

    class Meta:
        model = Library1
        fields = ['year','month']


class Library2Filter(django_filters.FilterSet):

    class Meta:
        model = Library2
        fields = ['year','month']

#Department filters
class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = StudentResult
        fields = ['department']

class DeptEvent1Filter(django_filters.FilterSet):
    class Meta:
        model = DeptEvent1
        fields = ['department']
        
class DeptProEvent3Filter(django_filters.FilterSet):
    class Meta:
        model = DeptProEvent3
        fields = ['department']
        
class DeptFacultyDev4Filter(django_filters.FilterSet):
    class Meta:
        model = DeptFacultyDev4
        fields = ['department']
        
class DeptStudPart5Filter(django_filters.FilterSet):
    class Meta:
        model = DeptStudPart5
        fields = ['department']
        
class ResProject1Filter(django_filters.FilterSet):
    class Meta:
        model = ResProject1
        fields = ['department']
        
class ResInternational3Filter(django_filters.FilterSet):
    class Meta:
        model = ResInternational3
        fields = ['department']
        
class ResNational4Filter(django_filters.FilterSet):
    class Meta:
        model = ResNational4
        fields = ['department']
        
class ConfInternational5Filter(django_filters.FilterSet):
    class Meta:
        model = ConfInternational5
        fields = ['department']
        
class ConfNational6Filter(django_filters.FilterSet):
    class Meta:
        model = ConfNational6
        fields = ['department']
        
class FacEvents8Filter(django_filters.FilterSet):
    class Meta:
        model = FacEvents8
        fields = ['department']
        
class ProfessionalPrac9Filter(django_filters.FilterSet):
    class Meta:
        model = ProfessionalPrac9
        fields = ['department']
        
class FacPatents10Filter(django_filters.FilterSet):
    class Meta:
        model = FacPatents10
        fields = ['department']
        
class NationalAttend11Filter(django_filters.FilterSet):
    class Meta:
        model = NationalAttend11
        fields = ['department']
        
class InternationalAttend12Filter(django_filters.FilterSet):
    class Meta:
        model = InternationalAttend12
        fields = ['department']
        
class FacAchieveFilter(django_filters.FilterSet):
    class Meta:
        model = FacAchieve
        fields = ['department']
        
class IndFacvisit1Filter(django_filters.FilterSet):
    class Meta:
        model = IndFacvisit1
        fields = ['department']
        
class IndInst2Filter(django_filters.FilterSet):
    class Meta:
        model = IndInst2
        fields = ['department']
        
class IndInst3Filter(django_filters.FilterSet):
    class Meta:
        model = IndInst3
        fields = ['department']
        
class IndInst4Filter(django_filters.FilterSet):
    class Meta:
        model = StudentResult
        fields = ['department']
        
class IndInst9Filter(django_filters.FilterSet):
    class Meta:
        model = IndInst9
        fields = ['department']
        
class CurGuestLect1Filter(django_filters.FilterSet):
    class Meta:
        model = CurGuestLect1
        fields = ['department']
        
class CurExptLect2Filter(django_filters.FilterSet):
    class Meta:
        model = CurExptLect2
        fields = ['department']
        
class CurStudTrain3Filter(django_filters.FilterSet):
    class Meta:
        model = CurStudTrain3
        fields = ['department']
        
class CurStudVisit4Filter(django_filters.FilterSet):
    class Meta:
        model = CurStudVisit4
        fields = ['department']
        
class StudFac1Filter(django_filters.FilterSet):
    class Meta:
        model = StudFac1
        fields = ['department']
        
class StudFac3Filter(django_filters.FilterSet):
    class Meta:
        model = StudFac3
        fields = ['department']
        
class ExtraAct6Filter(django_filters.FilterSet):
    class Meta:
        model = ExtraAct6
        fields = ['department']

#Placement Filters        
class Placement4Filter(django_filters.FilterSet):
    class Meta:
        model = Placement4
        fields = ['department']
        
