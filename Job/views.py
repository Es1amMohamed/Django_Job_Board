from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job
from .job_api import Job_Jason
from rest_framework import viewsets
from .forms import Apply_form



# Create your views here.

def job_list(request):
    joblist = Job.objects.all()
    paginator = Paginator(joblist,1)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs':page_obj}
    return render(request,'jobs/job_list.html',context)

def job_details(request,slug):
    jobdetails = Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = Apply_form(request.POST , request.FILES)
        if form.is_valid():
            mform = form.save(commit=False)
            mform.job = jobdetails
            mform.save()
           
         
    else:
            form = Apply_form()
    
    
    context = {'job':jobdetails , 'form':form}
    return render(request,'jobs/job_details.html',context)




class Jason_Job(viewsets.ModelViewSet):
        queryset = Job.objects.all()
        serializer_class = Job_Jason
   