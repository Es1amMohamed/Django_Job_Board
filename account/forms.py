
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )
        
class Formuser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',]

class Formprofile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','phone','email']