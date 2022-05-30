from authenticating.models import CustomUserManager
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)


class Ticheting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name='users')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)
    category =  models.ForeignKey(Category , on_delete=models.CASCADE , related_name='categories')
    description = models.TextField()


    def __str__(self):
        return str(self.title)


