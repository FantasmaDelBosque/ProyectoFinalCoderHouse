from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import  Ropa,Zapatos, Accesorios, Avatar 

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ("username", "email", "password1", "password2")

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("¡Las contraseñas no coinciden!")
        return password2


class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = ['nombre', 'descripcion', 'talla', 'marca','precio', 'imagen']

class ZapatosForm(forms.ModelForm):
    class Meta:
        model = Zapatos
        fields = ['nombre', 'descripcion', 'talla', 'marca','precio', 'imagen']

class AccesoriosForm(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ['nombre', 'descripcion', 'talla', 'marca','precio', 'imagen']



class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)
        widgets = {
            'imagen': forms.ClearableFileInput(),  # Elimina 'attrs' para 'multiple'
        }
