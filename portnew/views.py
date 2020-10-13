from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView # new
from .models import *
import io
from django.http import FileResponse
# Create your views here.

class PostPageView(ListView):
    model = Post
    template_name = 'slides.html'

class ImagePageView(ListView):
    model = Picture
    template_name = 'portnew/post.html'

class AboutPageView(ListView):
    model = About
    template_name = 'portnew/about.html'

class ProjectPageView(ListView):
    model = Project
    template_name = 'portnew/project.html'


def home(request):
    name = Users.objects.all()
    file_str = filestorage.objects.all()
    uploaded_file = filestorage.objects.get(id=1).file_up
    context = {'name': name, 'file_str': file_str, 'uploaded_file':uploaded_file}

    return render(request, 'portnew/home.html', context)


def contactme(request):
    context = {}
    return render(request, 'portnew/contact.html', context)

