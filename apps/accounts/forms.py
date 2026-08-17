from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.Form):
    
    username = forms.CharField(
        label='Username',
        
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: Jamshidbek'
            }
        ),
        required=True
        )