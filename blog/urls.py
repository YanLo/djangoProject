from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about1/', views.about, name='blog-about'),
]
