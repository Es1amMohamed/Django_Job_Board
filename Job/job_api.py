from .models import Job , Apply
from rest_framework import serializers

class Job_Jason(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title','Published_at']
        
class Apply_jason(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apply
        fields = ['name','email']