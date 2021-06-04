from django import forms

from .models import article

class aform(forms.ModelForm):
    class Meta:
        model = article
        fields = [
            'title', 
            'content', 
            'active',
        ]