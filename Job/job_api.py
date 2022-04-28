from .models import Job , Apply
from account.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class Job_Jason(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        
        fields = ['title']
        
        
class Apply_jason(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apply
        fields = ['name','email']