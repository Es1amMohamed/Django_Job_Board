from .models import Job
from rest_framework import serializers

class Job_Jason(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['id' , 'title']