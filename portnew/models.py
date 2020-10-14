from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Users"
    def __str__(self):
        return self.name

class Picture(models.Model):
    name = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name