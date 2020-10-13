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

class filestorage(models.Model):
    username = models.ForeignKey(Users, blank=True,null=True, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200, blank=True,null=True)
    time = models.DateTimeField(auto_now=timezone.now(), blank=True,null=True)
    file_up = models.FileField("File Upload",blank=True,null=True)

    class Meta:
        verbose_name_plural = "File Stored"
    def __str__(self):
        return self.file_name

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

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