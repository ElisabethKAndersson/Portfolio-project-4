from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from presentation.views import index, prices, contact
from presentation.views import leave_review, reviews, edit_review, delete_review


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('leave_review/', leave_review, name='leave_review'),
    path('edit/<item_id>', edit_review, name='edit_review'),
    path('delete/<item_id>', delete_review, name='delete'),
    path('reviews/', reviews, name='reviews'),
    path('prices/', prices, name='prices'),
    path('contact/', contact, name='contact'),
    path("accounts/", include("allauth.urls")),
]
