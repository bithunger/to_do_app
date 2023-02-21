from django.contrib import admin
from todotask.models import task

class taskAdmin(admin.ModelAdmin):
    list_display=('user','title','des','complete','user_slug','created')

admin.site.register(task, taskAdmin)
# Register your models here.
