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
