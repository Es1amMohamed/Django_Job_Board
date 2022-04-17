
from django.shortcuts import render
from .models import Job


# Create your views here.

def job_list(request):
    joblist = Job.objects.all()
    context = {'jobs':joblist}
    return render(request,'jobs/job_list.html',context)

def job_details(request,id):
    jobdetails = Job.objects.get(id=id)
    context = {'job':jobdetails}
    return render(request,'jobs/job_details.html',context)
   