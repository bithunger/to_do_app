from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib import messages


def index(request):
    return render(request, 'authentication/index.html')


def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist- try another")
            return redirect('register')
        
        if len(username)>10:
            messages.error(request, "Username must less then 10 character")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "Username only contain alphanumeric")
            return redirect('register')
        
        if User.objects.filter(email=email):
            messages.error(request, "This email already have an account- try another")
            return redirect('register')
        
        if pass1!=pass2:
            messages.error(request, "Password didn't match")
            return redirect('register')
        
        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname

        user.save()
        messages.success(request, 'Created')

        return redirect('login')

    return render(request, 'authentication/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)

        if user is not None:
            authlogin(request, user)
            if request.GET.get('next', None):
                return redirect(request.GET['next'])
            messages.success(request, f'Logged in')
            return redirect('home')
        else:
            messages.error(request, 'Bad credential')
            return redirect('login')

    return render(request, 'authentication/login.html')

def signout(request):
    logout(request)
    messages.success(request, "You are successfully Logged out")
    return redirect('login')

# Create your views here.
