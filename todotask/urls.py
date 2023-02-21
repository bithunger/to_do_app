from django.contrib import admin
from todotask import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('update/<slug>', views.update, name="update"),
    path('delete/<slug>', views.delete, name="delete"),
]
