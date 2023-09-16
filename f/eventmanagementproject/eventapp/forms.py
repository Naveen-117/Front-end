from django import forms
from .models import Apply

class AppForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','phone','email']
