import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


#--------------------------------------------------------
#Blog

#Formulario para Paginas
class Pagina_Form(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    cuerpo = forms.CharField(widget= CKEditorWidget)
    #autor = forms.CharField(max_length=200)
    autor = forms.ModelChoiceField(queryset=User.objects.all())  #Autor es un dropdown menu donde las opciones son  todos los objetos del modelo User
    fecha = forms.DateField(initial=datetime.date.today)
    imagen = forms.ImageField(label = 'Imagen', widget=forms.ClearableFileInput) #required=False