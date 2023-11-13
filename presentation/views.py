from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Item
from .forms import ItemForm
# from .forms import LeaveReview, Post
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


# Review page
def reviews(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'presentation/reviews.html', context)


def leave_review(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'leave_review', context)


def edit_review(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'presentation/reviews.html', context)


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('presentation/reviews.html')
