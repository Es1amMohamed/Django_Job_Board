from enum import auto
from random import choices
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

Job_Type = (
    ('Full Time' , 'Full Time'), 
    ('Part Time' , 'Part Time'),
)



class Job(models.Model):
    owner = models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE) 
    title = models.CharField(max_length= 40)
    description = models.TextField(max_length= 500)
    job_Responsibility = models.TextField(max_length= 1000)
    Published_at = models.DateTimeField(auto_now=True)
    type= models.CharField(max_length = 20 , choices = Job_Type)
    vacancy = models.IntegerField(default= 1 )
    salary = models.IntegerField(default= 0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', null=True ,blank=True,on_delete= models.CASCADE)  
    slug = models.SlugField(unique=True , null=True , blank=True)  
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
        
class Category(models.Model):
    name = models.CharField(max_length= 30)
    
    def __str__(self) :
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job,related_name= 'apply_job',on_delete=models.CASCADE,default = 1)
    apply_at = models.DateTimeField(auto_now= True)
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    url = models.URLField()
    cv = models.FileField(upload_to= 'upload/' )
    cover_letter = models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.name
    
    