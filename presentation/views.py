from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Item
from .forms import ItemForm
from django.core.paginator import Paginator
# from .forms import LeaveReview, Post



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
    list_reviews = Item.objects.all()

    p = Paginator(Item.objects.all(), 3)
    page = request.GET.get('page')
    reviews_list = p.get_page(page)
    nums = "a" * reviews_list.paginator.num_pages

    text =  {'list_reviews' : list_reviews,
                'reviews_list': reviews_list,
                'nums':nums}
        
    return render(request, 'presentation/reviews.html', text)


def leave_review(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ItemForm(request.POST)

           
            
            if form.is_valid():
                obj = form.save(commit=False) 
                obj.author_id = request.user.id
                obj.save() 
            else:
                print("ERROR : Form is invalid")
            
            return redirect('reviews')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'presentation/leave_review.html', context)


def edit_review(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'presentation/edit_review.html', context)


def delete_review(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('reviews')


# Booking page