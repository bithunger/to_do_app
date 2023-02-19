from django.shortcuts import render

def index(request):
    return render(request ,'authentication/index.html')

def login(request):
    return render(request ,'authentication/login.html')

def register(request):
    return render(request ,'authentication/register.html')

# Create your views here.
