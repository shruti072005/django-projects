
from django.contrib import admin
from django.urls import path
from bookingapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',homeview, name='home'),
    path('booking/', bookingview, name='booking'),
    path('display/', displayview, name='display'),
]
