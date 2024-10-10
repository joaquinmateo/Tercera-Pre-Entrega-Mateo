from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):

    password = forms.CharField(
       help_text="",
       widget=forms.MultipleHiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
       self.cleaned_data
       password1 = self.cleaned_data["password1"]
       password2 = self.cleaned_data["password2"]

       if password2 != password1:
          raise forms.ValidationError("Las contraseñas no son iguales")
       else:
          return password2

class OpinionFormulario(forms.Form):
    email = forms.EmailField()
    opinion = forms.CharField()