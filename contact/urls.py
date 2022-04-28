
from django.urls import path , include
from . import views
from .views import *

app_name = 'contact'
urlpatterns = [ 
    path('', views.contact,name = 'contact'),

]