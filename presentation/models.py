from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Item(models.Model):
    context = models.TextField(max_length=200, default="Add your review")
    name = models.CharField(max_length=30, default="Add your name")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews", default=1
    )

    def __str__(self):
        return self.name
