from django import forms
from .models import DocteurSignUp, Docteurs

class DoctorSignUp(forms.ModelForm):
    class Meta:
        model = DocteurSignUp
        fields = '__all__'

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = Docteurs
        fields = '__all__'