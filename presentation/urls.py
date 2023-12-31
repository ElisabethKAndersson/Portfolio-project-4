"""soulspark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from presentation.views import index, prices, contact
from presentation.views import leave_review, reviews, edit_review


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('leave_review/', leave_review, name='leave_review'),
    path('edit_review/', edit_review, name='edit_review'),
    path('reviews/', reviews, name='reviews'),
    path('prices/', prices, name='prices'),
    path('contact/', contact, name='contact'),
    path("accounts/", include("allauth.urls")),
]
