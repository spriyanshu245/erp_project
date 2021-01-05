from .models import *
from django.core import serializers


class ResProject1Serializer(serializers.ModelSerializer):
    Research_Project = serializers.SomeSerializerField(source='title')

    class Meta:
        model = ResProject1
        fields = ('id','Research Project','department', 'Principal Investigator','dates', 'Approval Agency','Any other Faculty')