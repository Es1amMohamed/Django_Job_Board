from enum import auto
from random import choices
from django.db import models
from django.utils.text import slugify

# Create your models here.

Job_Type = (
    ('Full Time' , 'Full Time'), 
    ('Part Time' , 'Part Time'),
)



class Job(models.Model):
    #owner 
    title = models.CharField(max_length= 40)
    description = models.TextField(max_length= 500)
    job_Responsibility = models.TextField(max_length= 1000)
    Published_at = models.DateTimeField(auto_now=True)
    type= models.CharField(max_length = 20 , choices = Job_Type)
    vacancy = models.IntegerField(default= 1 )
    salary = models.IntegerField(default= 0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', null=True ,blank=True,on_delete= models.CASCADE)  
    slug = models.SlugField(max_length=40 , unique= True , null=True , blank=True)  
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
        
class Category(models.Model):
    name = models.CharField(max_length= 30)
    
    def __str__(self) :
        return self.name
    