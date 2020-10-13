from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home,name='home'),
    path('posts', ImagePageView.as_view() ,name='post'),
    path('about', AboutPageView.as_view(),name='about'),
    path('project/', ProjectPageView.as_view(), name='project'),
]