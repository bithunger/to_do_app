from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    des = models.TextField()
    complete = models.BooleanField(blank=True, default=False)
    user_slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['complete']
