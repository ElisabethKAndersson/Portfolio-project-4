from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Item(models.Model):
    context = models.TextField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, blank=False, default=False)

    def __str__(self):
        return self.name
