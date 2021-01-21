from typing import Generic
from .models import *
from django.core import serializers


class ResProject1Serializer(serializers.Serializer):
    Research_Project = serializers.SomeSerializerField(source='title')

    class Meta:
        model = ResProject1
        fields = ('id','Research Project','department', 'Principal Investigator','dates', 'Approval Agency','Any other Faculty')


class StudentResultSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(StudentResult, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)

class StudentResultCreate(Generic.RetrieveAPIView):
        serializer_class = StudentResultSerializer(remove_fields=['department' 'Class'])