from django import forms
from .models import Vnoms

class VnomForm(forms.ModelForm):
    class Meta:
        model= Vnoms
        fields= '__all__'
        