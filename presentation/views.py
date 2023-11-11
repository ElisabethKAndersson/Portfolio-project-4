from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import ListView
from .models import Post

# Create your views here.


# Index page
def index(request):
    return render(request, "presentation/index.html")


# Review page
def reviews(request):
    return render(request, "presentation/reviews.html")


# Prices page
def prices(request):
    return render(request, "presentation/prices.html")


# Contact page
def contact(request):
    return render(request, "presentation/contact.html")


# Post mopdel to post review.
class ReviewsView(ListView):
    model = Post
    template_name = 'presentation/reviews.html'
    context_object_name = 'posts'
