from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

"""def index(request):
    return HttpResponse("Hello, world!")"""
def index(request):
    return render(request, "hello/index.html")

def fazza(request):
    return HttpResponse("Hello Fazza")
def teena(request):
    return HttpResponse("Hello  teena")
def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })
