from django import forms


class LeaveReview(forms.Form):
    comment = forms.CharField(max_length=400)
    name = forms.CharField(max_length=100)
