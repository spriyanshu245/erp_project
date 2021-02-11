import django_filters

from .models import *

class Place1Filter(django_filters.FilterSet):
    class Meta:
        model = Placement1
        fields = ['year',]