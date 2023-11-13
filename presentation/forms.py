from .models import Post
from django import forms
from django.db import models


#class LeaveReview(forms.Form):
#    comment = models.TextField(max_length=400)
#    name = forms.CharField(max_length=100)


class PostReview(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'author']
