
from django.contrib import admin
from django.urls import path
from bookingapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',homeview, name='home'),
    path('booking/', bookingview, name='booking'),
    path('display/', displayview, name='display'),
    path('update/<int:id>/', updateview, name='update'),
    path('delete/<int:id>/', deleteview, name='delete'),
]
   
