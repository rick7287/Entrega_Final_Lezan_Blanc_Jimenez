from django.db import models
from django.contrib.auth.models import User #hace falta o viene con la linea de arriba?
#para poder linkear User con Perfil:
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#mi RegisterForm me crea usuarios de User. aca intento extender al la info del Profile. 
class Perfil(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True) #q tenga los fields de User, mas los q agrego abajo. null=True hace falta?
    imagen= models.ImageField(upload_to='avatar', blank=True, null=True) # pide instalar Pillow. BLANK=TRUE, para q el ModelForm me tome required=False en el ModelForm!
    descripcion= models.TextField(blank=True, null=True) #default es Textarea...
    link= models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return str(self.user) #+'  '+self.contrasena+'  '+str(self.email)+'  '+str(self.link) #ROMPE.....asiq lo dejo asi.
    


#uso signals para linkear model User con Pefil:  
@receiver(post_save, sender=User) #si creo un User me crea un Perfil.   
def create_user_perfil(sender, instance, created, **kwargs): 
    if created:
        Perfil.objects.create(user=instance)

'''@receiver(post_save, sender=User) #si guardo un User me guarda el Perfil
def save_user_perfil(sender, instance, **kwargs): # uso save_user_profile. 
    instance.Perfil.save()   '''

#hace falta o no xq ya tengo el campo ImageField en Perfil!
'''class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.Cascade)
    imagen'''
