from django.shortcuts import render,HttpResponse

# Create your views here.


def greater(request):
    x, y = 12, 20
    greater_val = x if x > y else y
    return HttpResponse(f"The greater number between {x} and {y} is {greater_val}")

def is_even(request):
    num = 15
    if num % 2 == 0:
        return HttpResponse(f"{num} is Even")
    else:
        return HttpResponse(f"{num} is Odd")
