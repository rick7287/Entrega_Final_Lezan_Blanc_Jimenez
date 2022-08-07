from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega1.models import * #importo todas las clases de models 
from AppEntrega1.forms import * #y las de los formularios

#creo las vistas, una por cada html. salvo la del padre.html q no va.

def inicio(request):   
    return render(request, 'AppEntrega1/inicio.html')

def bodega(request):   
    return render(request, 'AppEntrega1/bodega.html')

def vino(request):   
    return render(request, 'AppEntrega1/vino.html')

def cliente(request):   
    return render(request, 'AppEntrega1/cliente.html')

#ahora faltan las de los forms.
def bodegaFormulario(request):   #creo la vista de bodegaFormulario
    if (request.method=='POST'):
        form= BodegaForm(request.POST) #asi me llega la info del html.
        if form.is_valid():   #si pasa la validacion de django...
            info=form.cleaned_data #limpio la info de form, y me lo da como dicct
            nombre=info['nombre']
            email=info['email']
            bodega=Bodega(nombre=nombre, email=email) #ie creo un objeto de mi clase, con los valores q me vienen por POST
            bodega.save()
            return render(request, 'AppEntrega1/inicio.html') #me lleva al inicio, cuando entra en este if!
    else:
        form=BodegaForm() #formulario vacio,
    return render(request, 'AppEntrega1/bodegaFormulario.html', {'form':form})   
        #osea lo renderizo y se lo mando como dicct para q lo use el template, como q se hace por POST??  

#hago las 2 q faltan iguales. 
def vinoFormulario(request):   #NO FUNCIONA X EL CAMPO BODEGAAA...!!!?
    if (request.method=='POST'):
        form= VinoForm(request.POST)
        if form.is_valid():   
            info=form.cleaned_data 
            nombre=info['nombre']
            varietal=info['varietal']
            bodegaa=info['bodegaa']
            vino=Vino(nombre=nombre, varietal=varietal, bodegaa=bodegaa)
            vino.save()
            return render(request, 'AppEntrega1/inicio.html') 
    else:
        form=VinoForm() 
    return render(request, 'AppEntrega1/vinoFormulario.html', {'form':form}) 
#clienteForm
def clienteFormulario(request):   
    if (request.method=='POST'):
        form= ClienteForm(request.POST)
        if form.is_valid():   
            info=form.cleaned_data 
            nombre=info['nombre']
            email=info['email']
            pais=info['pais']
            cliente=Cliente(nombre=nombre, email=email, pais=pais)
            cliente.save()
            return render(request, 'AppEntrega1/inicio.html') 
    else:
        form=ClienteForm() 
    return render(request, 'AppEntrega1/clienteFormulario.html', {'form':form})

#ahora el formulario de busqueda
def busquedaCliente(request):
    return render(request, 'AppEntrega1/busquedaCliente.html')

def buscar(request):
    if request.GET['nombre']: #ie si hay algo.
        nombre= request.GET['nombre']
        clientes=Cliente.objects.filter(nombre= nombre)#filtra todos los clientes con el request
        respuesta= f'estoy buscando los clientes con el nombre:{cliente}'
        return render(request, 'AppEntrega1/resultadosBusqueda.html', {'clientes':clientes})
    else:
        return render(request, 'AppEntrega1/busquedaCliente.html', {'error':'no se ingreso un cliente'})



# dejo estas vistas viejas como comentario por si las necesito. 
'''def bodega(self):
    bodega=Bodega(nombre='Santa Julia', email= santajulia@santajulia.com)
    bodega.save()
    texto=f'bodega {bodega.nombre}, email {bodega.email}'
    return HttpResponse(texto)

def vino(self):
    vino=Vino(nombre='GranPinot', varietal= 'pinot', bodega='Trapiche')
    vino.save()
    texto=f'Vino {vino.nombre}, varietal {vino.varietal}, de bodega {vino.bodega}'
    return HttpResponse(texto)

def cliente(self):
    cliente=Cliente(nombre='Gerardo Morales', email=gm@gm.com, pais='Ecuador')
    cliente.save()
    texto=f'cliente {cliente.nombre}, email: {cliente.email}, pais: {cliente.pais}'
    return HttpResponse(texto)'''