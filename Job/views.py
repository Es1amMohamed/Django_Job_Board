from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job



# Create your views here.

def job_list(request):
    joblist = Job.objects.all()
    paginator = Paginator(joblist,1)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs':page_obj}
    return render(request,'jobs/job_list.html',context)

def job_details(request,id):
    jobdetails = Job.objects.get(id=id)
    context = {'job':jobdetails}
    return render(request,'jobs/job_details.html',context)
   