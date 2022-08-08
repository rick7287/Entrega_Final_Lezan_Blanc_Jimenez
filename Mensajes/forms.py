import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

##Creacion de mensajes:

class MensajeForm(forms.Form):
    emisor= forms.CharField (max_length=50)
    receptor= forms.CharField (max_length=50)
    message= forms.CharField(max_length=300)
    fecha= forms. DateField()
    hora= forms.TimeField()