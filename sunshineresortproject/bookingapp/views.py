
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking

class BookingViews:
    def home(self, request):
        return render(request, 'bookingapp/index.html')

    def create(self, request):
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
        return render(request, 'bookingapp/booking.html')

    def display(self, request):
        bookings = Booking.objects.all()
        return render(request, 'bookingapp/display.html', {'bookings': bookings})

    def update(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        if request.method == 'POST':
            booking.name = request.POST.get('name')
            booking.email = request.POST.get('email')
            booking.checkin = request.POST.get('checkin')
            booking.checkout = request.POST.get('checkout')
            booking.roomtype = request.POST.get('roomtype')
            booking.guests = request.POST.get('guests')
            booking.save()
            return redirect('display')
        return render(request, 'bookingapp/update.html', {'booking': booking})

    def delete(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        if request.method == 'POST':
            booking.delete()
            return redirect('display')
        return render(request, 'bookingapp/delete.html', {'booking': booking})
    

