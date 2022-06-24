from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        #Para ocupar todos los campos de libro en modls.py
        fields = '__all__'