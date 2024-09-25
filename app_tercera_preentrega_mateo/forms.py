from django import forms

class formulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class critica(forms.Form):
    critica = forms.CharField()