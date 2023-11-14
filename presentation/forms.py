from django import forms
from django.db import models
from .models import Item

# class LeaveReview(forms.Form):
#    comment = models.TextField(max_length=400)
#    name = forms.CharField(max_length=100)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['context', 'name', 'author']
