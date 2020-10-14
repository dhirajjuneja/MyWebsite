from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView # new
from .models import *
import io
from django.http import FileResponse
# Create your views here.

class HomePageView(ListView):
    model = Picture
    template_name = 'portnew/home.html'

class AboutPageView(ListView):
    model = About
    template_name = 'portnew/about.html'

class ProjectPageView(ListView):
    model = Project
    template_name = 'portnew/project.html'

