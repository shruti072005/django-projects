
from django.contrib import admin
from django.urls import path

# Import views from both apps with aliases
from calculator import views
from comparator import view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.add, name='add'),
    path('sub/',views.sub, name='sub'),
    path('div/',views.div, name='adiv'),
    path('mult/',views.mult, name='mult'),
    
       path('greater/',view.greater, name='greater'),
    path('iseven/',view.is_even, name='iseven'),
    
]

