from django import forms
from .models import EntryCategory, Matter

class CallForm(forms.Form):

    matter = forms.ModelChoiceField(queryset=Matter.objects.all())
    category = forms.ModelChoiceField(queryset=EntryCategory.objects.filter(type=3))
    description = forms.CharField(required=False)
    length = forms.DecimalField(max_digits=2)
    notes = forms.CharField(widget=forms.Textarea)
