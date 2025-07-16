
from django.contrib import admin
from django.urls import path,include
from resume.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('resume.urls')), 
]

    