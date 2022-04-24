"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from Job import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.Jason_Job)
router2 = routers.DefaultRouter()
router2.register(r'users',views.Jason_apply)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('account.urls', namespace= 'account')),
    path('admin/', admin.site.urls),
    path('jason/', include(router.urls)),
    path('jason2/', include(router2.urls)),
    path('', include('Job.urls', namespace= 'jobs')),
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
