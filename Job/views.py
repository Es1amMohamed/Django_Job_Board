from django.shortcuts import render


# Create your views here.

def job_list(request):
    return render(request,'jobs.html')

def job_details(request):
    pass
