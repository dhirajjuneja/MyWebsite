from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('about', AboutPageView.as_view(),name='about'),
    path('project/', ProjectPageView.as_view(), name='project'),
]