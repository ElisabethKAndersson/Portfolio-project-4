from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    content = models.TextField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def author_id():
        return get_user_model()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review", default=author_id)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
