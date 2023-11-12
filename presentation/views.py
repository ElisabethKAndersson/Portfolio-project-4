from django.shortcuts import render, get_object_or_404
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
class ReviewsView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'presentation/reviews.html'
    context_object_name = 'posts'
    paginate_by = 4
