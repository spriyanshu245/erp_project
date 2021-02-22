import django_filters

from .models import *

class Place1Filter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(Place1Filter, self).__init__(*args, **kwargs)
        self.form.initial['year'] = 2021

    class Meta:
        model = Placement1
        fields = ['year']