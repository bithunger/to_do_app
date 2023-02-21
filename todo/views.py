# from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login as authlogin, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# @login_required(login_url='login')
# def home(request):
#     fname = request.user.first_name
#     return render(request, 'todolist/home.html', {'fname':fname})