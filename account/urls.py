
from django.urls import path , include
from . import views
from .views import *

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
]
