from enum import auto
from random import choices
from django.db import models

# Create your models here.

Job_Type = (
    ('Full Time' , 'Full Time'), 
    ('Part Time' , 'Part Time'),
)

Category = (
    ('Frontend Developer','Frontend Developer'),
    ('Backend Developer','Backend Developer'),
)

class Job(models.Model):
    #owner 
    title = models.CharField(max_length= 40)
    description = models.TextField(max_length= 500)
    job_Responsibility = models.TextField(max_length= 1000)
    category = models.CharField(max_length = 50 ,choices=Category)
    Published_at = models.DateTimeField(auto_now=True)
    type= models.CharField(max_length = 20 , choices = Job_Type)
    vacancy = models.IntegerField(default= 1 )
    salary = models.IntegerField(default= 0)
    experience = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title