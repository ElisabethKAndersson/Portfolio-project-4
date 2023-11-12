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
def leave_review(request, post):
    comment_form = Post(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
    else:
        comment_form = Post()

    return render(
        request, post, "reviews.html",
        {'comments': comments,
         'form': comment_form},
    )
