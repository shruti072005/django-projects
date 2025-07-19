from django.shortcuts import render,redirect
from .models import Booking   

# Create your views here.
def homeview(request):
    return render(request, 'bookingapp/index.html')

def bookingview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        roomtype = request.POST.get('roomtype')
        guests = request.POST.get('guests')

        booking = Booking(
            name=name,
            email=email,
            checkin=checkin,
            checkout=checkout,
            roomtype=roomtype,
            guests=guests
            
        )
        booking.save()
        
        return redirect('home')
        #return render(request, 'bookingapp/booking.html', {'booking': booking})
    return render(request, 'bookingapp/booking.html')

def displayview(request):
    bookings = Booking.objects.all()
    return render(request, 'bookingapp/display.html', {'bookings': bookings})
