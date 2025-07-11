from django.shortcuts import render,HttpResponse

# Create your views here.

def add(request):
    a,b=10,20
    result = a + b
    return HttpResponse(f"Addition of {a} and {b} is {result}")

def sub(request):
    a,b=10,20
    result = a - b
    return HttpResponse(f"subtraction of {a} and {b} is {result}")

def div(request):
    a,b=10,20
    result = a / b
    return HttpResponse(f"division of {a} and {b} is {result}")

def mult(request):
    a,b=10,20
    result = a * b
    return HttpResponse(f"Multiplication of {a} and {b} is {result}")
