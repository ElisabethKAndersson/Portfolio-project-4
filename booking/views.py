from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from presentation.models import Item
from presentation.forms import ItemForm


# Booking page
def booking(request):
    return render(request, "booking.html")