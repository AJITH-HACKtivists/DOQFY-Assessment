from django import forms
from .models import SnippetModel

class SnippetModelForm(forms.ModelForm):
    class Meta():
        model = SnippetModel
        fields = ['text','secret_key']
        labels = {
            'text': 'Enter Text',
            'secret_key': 'Enter the secret Key'
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Please enter text',
                'class': 'form-control text-field', 
                'rows': 4,  
                'cols': 40  
            }),
            'secret_key':forms.PasswordInput(attrs={
                'placeholder': 'Please enter Secret Key (Optional)',
                'class': 'form-control secret-key'  # Optional: to apply Bootstrap styles or other CSS classes
            })
        }
        error_messages = {
            'text': {
                'required': 'Please enter proper text.',
                'invalid':'Please Enter Valid Data'
            }
        }


    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(str(text).strip()) == 0:
            raise forms.ValidationError('Text must be at least 5 characters long.')
        return text
