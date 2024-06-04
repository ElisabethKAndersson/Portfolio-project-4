from django import forms
from django.db import models
from .models import Item


#  Form for leaving a review

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['context', 'name']

