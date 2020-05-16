from django import forms

class SortForm(forms.Form):
    CHOICES = (('name', 'Name'),('author', 'Author'),('publishedAt', 'Date & Time'))
    sort = forms.ChoiceField(choices=CHOICES)
    descending = forms.BooleanField(required=False)
