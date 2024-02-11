from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from booking import views

urlpatterns = [
path('booking/', views.booking, name='booking')
]