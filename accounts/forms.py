from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm #revisar capas ya no al necesito.
from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _
from .models import Perfil

#forms para Register(crea User), Login y Editar User:

'''#uso ModelForm q es mas rapido. pero menos customizable....
class UserForm(forms.ModelForm): #podria ser hijo de UserCreationForm tmb!
    class Meta:
        model = User
        fields = ('username', 'email', 'password') #OJO SI ROMPRE CAMBIAR userame a first_name... 
        #labels={'username':_('usuario'), 'password':_('constrasena')}. IDEM CON HELPTEXTS..'''
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('imagen', 'descripcion', 'link') #OBS: no inlcuyo el user. 
        help_texts = {'link': ('debes poner http://'),}
        #obs no le puse ningun label al field imagen. (ricardo le puso Picture al suyo)

#form para crear Usuario: en consigna, solo pide los campos username, email, pswd. 
class UserRegisterForm(UserCreationForm):
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'campos obligatorios' for k in fields}  #igual me los esta dejando vacios...?

#esta capaz no lo necesito:
class UserEditForm(UserCreationForm):
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'campos obligatorios' for k in fields} 

'''#form para crear perfiles con los demas campos:       
class ProfileCreationForm(UserRegisterForm): #o q sea hijo de UserCreationForm?

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields} #me pone vacios los help_texts en estos campos.'''

'''#form para el model Perfil:
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen', 'descripcion','link'] #no incluyo el user porq lo tengo del otro form. '''

'''class PerfilForm(forms.Form): 
    #no incluyo user xq ya me lo pide en el otro form
    imagen= forms.ImageField(required=False) # pide instalar Pillow. o required=False?
    descripcion= forms.CharField(initial='describite aqui:', widget=forms.Textarea, required=False)
    link= forms.URLField(initial='https://', max_length=200, required=False)'''
    





#forms para Profile:
#DEBERIA PODER llegar a tener solo un form pada Editar, q sea para TODOS los campos....
#VER: como vinculo un form del model Perfil, con uno de UserCreationForm.(ie, de model User)....!!
#necesito uno nuevo?? o uso el de User??
'''class ProfileEditForm(UserCreationForm): #o simplemente con forms.Form? pero tiene q auntheticate, osea q deberia ser este. 
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    #agrego los otros campos: foto, descripcion, link web:
    imagen=forms.ImageField(required=False) #pide instalar Pillow...OK con pip install.
    descripcion=forms.CharField(initial='describite aqui:', widget=forms.Textarea, required=False)
    link=forms.URLField(initial='https://', max_length=200, required=False) # required=False para q no sean obligatorios.
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields} #me pone vacios los help_texts en estos campos.'''
   
