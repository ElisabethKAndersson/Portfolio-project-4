from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


# Index page
def index(request):
    return render(request, "presentation/index.html")


# Prices page
def prices(request):
    return render(request, "presentation/prices.html")


# Contact page
def contact(request):
    return render(request, "presentation/contact.html")


# Post model to post review.
