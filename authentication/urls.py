from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('signout/', views.signout, name="signout"),
]