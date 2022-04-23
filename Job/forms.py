
from django import forms
from .models import *



class Apply_form(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email','url','cv','cover_letter']