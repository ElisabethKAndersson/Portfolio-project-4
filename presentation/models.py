from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    content = models.TextField(max_length=300)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_post", default="user")

    def __str__(self):
        return self.content
