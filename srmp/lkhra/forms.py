from django import forms
from .models import Lkhra

class wakha(forms.ModelForm):
    class Meta:
        model= Lkhra
        fields= '__all__'
        