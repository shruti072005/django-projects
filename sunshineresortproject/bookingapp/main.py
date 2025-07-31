from django.shortcuts import render

def index(request):
    return render(request, 'bookingapp/index.html')

def booking(request):
    return render(request, 'bookingapp/booking.html')

def display(request):
    return render(request, 'bookingapp/display.html')

def update(request):
    return render(request, 'bookingapp/update.html')

def delete(request):
    return render(request, 'bookingapp/delete.html')
