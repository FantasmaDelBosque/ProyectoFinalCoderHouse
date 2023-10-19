from django import forms
from .models import  Ropa 

class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = ['nombre', 'descripcion', 'talla', 'marca','precio', 'imagen']