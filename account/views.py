import re
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import Profile

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/profile')
            
    else:
        form = SignUpForm()
        
    return render(request,'registration/signup.html',{'form':form})


def profile(request):
    
    profile = Profile.objects.get(user=request.user)

    return render(request,'account/profile.html',{'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        userform = Formuser(request.POST,instance=request.user)
        formprofile = Formprofile(request.POST,instance=profile)
        if userform.is_valid() and formprofile.is_valid():
            userform.save()
            myprofile = formprofile.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('account:profile'))
        
    else:
        userform = Formuser(instance=request.user)
        formprofile = Formprofile(instance=profile)
        context = {
            'userform':userform,
            'formprofile':formprofile,
        }
        
    return render(request,'account/profile_edit.html',context)
        