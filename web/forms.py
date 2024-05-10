from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TextInputWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'type': 'text'}
        super().__init__(*args, **kwargs)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['customer_name','customer_email','phone','message']
        widgets = {
            'customer_email': TextInputWidget(),  # Usa el widget personalizado
        }

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1','password2']
