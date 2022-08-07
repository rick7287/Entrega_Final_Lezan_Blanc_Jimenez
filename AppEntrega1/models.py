from django.db import models

# Create your models here.
class Bodega(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.nombre+'  '+str(self.email)

class Vino(models.Model):
    nombre=models.CharField(max_length=50)
    varietal=models.CharField(max_length=50)
    #bodegaa=models.CharField(max_length=50)  #le puse 'bodegaa'a ver si desaparece el error.O LE SACAMOS ESTE CAMPO Y CHAU 
    def __str__(self):
        return self.nombre+'  '+self.varietal+' '

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    pais=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre+'  '+str(self.email)+' '+self.pais