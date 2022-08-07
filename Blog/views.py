from django.shortcuts import render, redirect
from django.http import HttpResponse
from Blog.models import *
from Blog.forms import *

#Para el login

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    return render (request, 'Blog/inicio.html')


def redirect_view(request):
    response = redirect('/Blog/pages/')
    return response
#-----------------------------------------------------------------------------------------------
#BLOG


def paginas_ver(request):

    
    mensaje = ""
    paginas = Pagina.objects.all()                      #Traemos todos los objetos dentro de la tabla Paginas y los guardamos en la var paginas

    if not paginas:
            mensaje = 'Aun no hay entradas de Blog'
    

    contexto={'paginas':paginas, 'mensaje':mensaje}  
    # Creamos el contexto. Recuerda, esto es un diccioanrio, la clave o key es el nombre de nuestra variable. Los valores de nuestra variable son 
    # la lista de objetos que jalamos de la tabla

    return render(request, 'Blog/pages.html', contexto)




@login_required
def pagina_crear(request):

    mensaje=''
    
    
    if (request.method == "POST"):     
        formulario =Pagina_Form(request.POST, request.FILES)
        #formulario.autor = request.user

        if formulario.is_valid():            
            informacion = formulario.cleaned_data   

            titulo = informacion['titulo']
            subtitulo = informacion['subtitulo']
            cuerpo = informacion['cuerpo']

            #Puedo sacar autor de la info del form porque desde que cree mi form defini las opciones del campo autor como instancias del modelo User
            #Si no lo hago asi (definir el campo como un CharField por ejemplo), al tratar de salvar el objeto 'pagina' me da un error, porque iba 
            #a tratar de mandar un str cuando el modelo indica que debe ser una instance de User
            autor = informacion['autor']
            fecha = informacion['fecha']
            imagen = informacion['imagen']
                        
            pagina = Pagina(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)  
            pagina.save()
            mensaje = f"La pagina {pagina.titulo} se ha creado  exitosamente"
            return render(request, "Blog/pagina_crear.html", {"formulario":formulario,'mensaje':mensaje})              
            #return render(request, "Blog/pages.html", {'mensaje':mensaje})              
            #return render(request, "Blog/inicio.html") 
        else:
            mensaje='Error con el formulario'
            return render(request, "Blog/pagina_crear.html", {"formulario":formulario, 'mensaje':mensaje})

    else: 
        formulario= Pagina_Form( initial={'autor':request.user})  
        #Estoy personalizando el campo 'autor' de mi formulario. Le estoy diciendo que las opciones que va a mostrar no son todos los users, sino solo el user de quien esta logeado.
        formulario.fields['autor'].queryset= User.objects.filter(username=request.user)

    return render(request, "Blog/pagina_crear.html", {"formulario":formulario, 'mensaje':mensaje})


@login_required
def pagina_borrar(request, pagina_id):            #Cuando mando llamar la vista, le paso un parametro, en este caso el id de una pagina

    mensaje = ""
    pagina = Pagina.objects.get(id=pagina_id)     #De la tabla/model Pagina, obtengo el objeto/registro que cumple con mi parametro
    pagina.delete()                               #Y lo borro

    #Vuelvo al menu, es decir, renderizo la html de leer paginas con la nueva lista de paginas
    paginas = Pagina.objects.all()                #Trae todas los paginas
    mensaje= f'La pagina {pagina.titulo} se elimino'

    contexto={'paginas':paginas, 'mensaje':mensaje}

    return render(request, 'Blog/pages.html', contexto)


@login_required
def pagina_editar(request, pagina_id):

    mensaje = ""
    pagina = Pagina.objects.get(id=pagina_id)
    #imagen = request.FILES.get(pagina.imagen.url)

    if (request.method == "POST"):
        formulario =Pagina_Form(request.POST, request.FILES)
        #imagen = request.FILES.get()

        
        if formulario.is_valid():   

            

            informacion = formulario.cleaned_data   
            pagina.titulo = informacion["titulo"]
            pagina.subtitulo = informacion["subtitulo"]
            pagina.cuerpo = informacion["cuerpo"]
            pagina.autor = informacion["autor"]
            pagina.fecha = informacion["fecha"]
            pagina.imagen = informacion["imagen"]
            pagina.save()

            mensaje = f"La pagina {pagina.titulo} se ha modificado  exitosamente"
            return render(request, "Blog/pages.html", {"formulario":formulario,'mensaje':mensaje})       
            #return render(request, "Blog/inicio.html") #Vuelvo al inicio o a donde quieran


    else: 
        #Creo el formulario con los datos que voy a modificar
        #formulario= Pagina_Form(instance = pagina)
        formulario= Pagina_Form(initial={'titulo': pagina.titulo, 'subtitulo':pagina.subtitulo, 'cuerpo':pagina.cuerpo, 'autor':pagina.autor, 'fecha':pagina.fecha, 'imagen':pagina.imagen})
        formulario.fields['autor'].queryset= User.objects.filter(username=request.user) 
        

    return render(request, "Blog/pagina_editar.html", {"formulario":formulario, "pagina":pagina, 'mensaje':mensaje})    
#Hay que mandar el "profesor_nombre":profesor_nombre para , "profesor_nombre":profesor_nombre


def pagina_detalle(request, pagina_id):

    #pagina = Pagina.objects.get(id=pagina_id)
    pagina = Pagina.objects.get(id=pagina_id)
     

    return render(request, "Blog/pagina_detalle.html", {"pagina":pagina})

    









    




#-----------------------------------------------------------------------------------------------
