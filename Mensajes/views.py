from email import message
from django.shortcuts import render 
from django.http import HttpResponse
from Mensajes.models import * 
from Mensajes.forms import *


# Create your views here.

def mensajes(request):   
    if (request.method=='POST'):
        form= MensajeForm(request.POST) 
        if form.is_valid():   
            info=form.cleaned_data
            emisor=info['emisor']
            receptor=info['receptor']
            message=info['message']
            fecha=info['fecha']
            hora=info['hora']
            mensaje=Mensajes(emisor=emisor,receptor= receptor, message=message, fecha=fecha, hora=hora ) 
            mensaje.save()
            coemntario = f"Su mensaje se ha enviado exitosamente"
            return render(request, 'Blog/inicio.html') 
    else:
        form=MensajeForm() 
    return render(request, 'Mensajes/inbox.html', {"form":form})