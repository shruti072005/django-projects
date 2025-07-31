
from django.contrib import admin
from django.urls import path
from bookingapp.views import BookingViews

views = BookingViews()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home, name='home'),
    path('booking/', views.create, name='booking'),
    path('display/', views.display, name='display'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
   
  