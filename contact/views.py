from django.conf import settings
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    myinfo = Info.objects.last()
    
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            
    )   
    
    return render(request,'contact/contact.html',{'myinfo':myinfo})
