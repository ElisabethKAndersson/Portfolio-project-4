from django import forms
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'created_on', 'author ']
