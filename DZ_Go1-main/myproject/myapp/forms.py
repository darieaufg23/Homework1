from django import forms
from .models import Home

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['first_name', 'last_name', 'date_of_birth', 'email']
