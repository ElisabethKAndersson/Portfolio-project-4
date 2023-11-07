from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic


# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def index(request):
    return render(request, "presentation/index.html")


def reviews(request):
    context = {
        'posts': posts
    }
    return render(request, "presentation/reviews.html", context)
