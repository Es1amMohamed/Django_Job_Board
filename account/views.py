from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            print('gg')
            login(request,user)
            print('gg')
            return redirect('/accounts/profile')
            
    else:
        form = SignUpForm()
        
    return render(request,'registration/signup.html',{'form':form})