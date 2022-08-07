from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = RichTextField(blank=True, null = True)
    #cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self):
            return self.titulo + " | " + str(self.autor)