from django import forms

# las clases de Formulario, heredadas de forms
class BodegaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()

class VinoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    varietal=forms.CharField(max_length=50)
    bodegaa=forms.CharField(max_length=50)

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    pais=forms.CharField(max_length=50)