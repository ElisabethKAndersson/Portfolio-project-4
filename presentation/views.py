from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic


# Create your views here.


def index(request):
    return render(request, "presentation/index.html")

def reviews(request):
    return render(request, "presentation/reviews.html")

