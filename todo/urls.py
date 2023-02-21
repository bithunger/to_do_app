from django.contrib import admin
from todo import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('home/', include('todotask.urls')),
]
