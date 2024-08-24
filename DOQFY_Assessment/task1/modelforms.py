from django import forms
from .models import UrlModel

class UrlModelForm(forms.ModelForm):
    class Meta:
        model = UrlModel
        fields = ['url']
        labels = {
            'url': 'Enter URL'
        }
        widgets = {
            'url': forms.URLInput(attrs={
                'placeholder': 'Please enter URL',
                'class': 'form-control'  # Optional: to apply Bootstrap styles or other CSS classes
            })
        }
        error_messages = {
            'url': {
                'required': 'Please provide a URL address.',
                'invalid': 'Enter a valid URL format.',
                'unique': 'Url Already Exists.'
            }
        }