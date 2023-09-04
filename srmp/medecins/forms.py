from django import forms
from .models import DocteurSignUp

class DoctorSignUp(forms.ModelForm):
    class Meta:
        model = DocteurSignUp
        fields = '__all__'