from django import forms
from django.forms import widgets

from .models import product

class productform(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Your title'}
        )
    )
    price = forms.DecimalField(decimal_places=2, max_digits=24, initial=420.69)
    email = forms.EmailField()


    class Meta:
        model = product
        fields = [
            'title', 
            'description', 
            'price', 
            'available',
        ]

     
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'v' in title:
            raise forms.ValidationError('v not found in title')
        return title




# class rawproductform(forms.Form):
#     title = forms.CharField(
#         widgets=forms.TextInput(attrs={'placeholder': 'Your title'})
#     )
#     description = forms.TextField(blank=True, null=True)
#     price = forms.DecimalField(decimal_places=2, max_digits=24)
#     available = forms.BooleanField(default=False)