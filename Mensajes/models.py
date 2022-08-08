from django.db import models
from django.contrib.auth.models import User


from ast import Return

# Create your models here.

class Mensajes (models.Model):
    emisor= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sender')
    receptor= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='receiver')
    message= models.CharField(max_length=300)
    fecha= models.DateField()
    hora= models.TimeField()

    def __str__ (self):
        return self.emisor+" "+self.receptor+" "+self.message+" "+self.fecha+" "+self.hora

