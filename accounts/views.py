from django.shortcuts import render, redirect #el redirect capaz no lo uso. 
from django.http import HttpResponse
from accounts.models import * #solo es Perfil! 
from accounts.forms import *  #importo todos xq igual son pocos. 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib import messages #podria no usarlo pero ya esta...
# Create your views here.

#vista home de accounts: hace falta?
def inicio(request):   
    return render(request, 'accounts/inicio.html')


#login. 
def login_request(request):
    #aagregar q si ya estoy logueado no entre??, muestre cartel"ya estas logueado", y me mande a donde estaba.(igual el boton ya esta ok login/logout)
    if request.method=='POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= request.POST['username'] 
            clave= request.POST['password'] 
            user=authenticate(username=usuario, password=clave)
            if user is not None: #ie si hace match con alguno
                login(request, user) 
                return render(request, 'accounts/inicio.html', {'form':form, 'mensaje':f'bienvenido  {usuario}'})
            else:
                return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'usuario o clave incorrecta'})    
        else:
            return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'FORMULARIO INVALIDO'} )
    else:  #si es GET
        form=AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form}) #lo mando al login con el form vacio

#registro. Obs: guarda en model User, pero esta linkeado en models, con el post_save, ent guarda tmb en Perfil.
def register(request):
    if request.method=='POST':
        formulario=UserRegisterForm(request.POST) 
        if formulario.is_valid():
            username=formulario.cleaned_data['username'] 
            email=formulario.cleaned_data['email'] #medio al pedo me estoy guardando email y contrasena aca?, xq no tengo q hacer authenticate.
            contrasena=formulario.cleaned_data['password1'] 
            formulario.save()
            form= AuthenticationForm(request, data=request.POST) #agrego este aca, para q despues del signup, me use el form de login, instanciado para q llene ya el username.  
            return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'usuario creado:{username} AHORA LOGUEATE!' })
    else:
        form=UserRegisterForm() 
    return render(request, 'accounts/signup.html', {'form':form})
    

@login_required
#@transaction.atomic. hace q se guarden ambos objetos o ninguno... (por si alguno falla, q el otro no se actualice)
def update_perfil(request): 
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user) #cambio UserForm por UserEditForm
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil) #le agregue aca el request.FILES. OJO VER XQ CAPAZ HAY Q AGREGARLO ANTES, EN EL UserCreation???
        #uso ambos forms a la vez y los valido:
        if user_form.is_valid() and perfil_form.is_valid():
            usuario=user_form.save()  #me guardo usuario asi lo paso por contexto..
            perfil_form.save()
            #messages.success(request, 'TU PERFIL HA SIDO ACTUALIZADO!') 
            return render(request, 'accounts/profile.html', {'usuario':usuario, 'mensaje':'TU USUARIO HA SIDO ACTUALIZADO','user_form': user_form, 'perfil_form': perfil_form})#redirect('settings:profile')
        else:
            messages.error(request, 'Fijate este error!:') #tmb podria pasarle return render(...mensage)
    else:
        user_form = UserEditForm(instance=request.user) #hace falta q vayan instanciados aca. es para q me los autorrellene?
        perfil_form = PerfilForm(instance=request.user.perfil)
    return render(request, 'accounts/update_perfil.html', {'user_form': user_form, 'perfil_form': perfil_form })





#nueva vista para VER mi perfil:
@login_required
def ver_perfil(request):
    user_form = UserEditForm(instance=request.user) 
    perfil_form = PerfilForm(instance=request.user.perfil)
    return render(request, 'accounts/profile.html',{'user_form': user_form, 'perfil_form': perfil_form } )


#para ver perfil sin formulario
@login_required
def info_perfil(request):
    usuario = request.user
    perfil = Perfil.objects.get(user = usuario)
    
    

    return render(request, 'accounts/perfil.html', {'perfil':perfil})






#vista para eliminar usuario.
@login_required
def deleteUser(request, usuario):
    usu=request.user 
    usu.delete()
    return render(request, 'accounts/inicio.html', {'mensaje':'Su usuario ha sido eliminado'}) #si se elimina, lo mando al inicio
        #desp de eliminar, todabia me muestra el 'hola user'y el LOGOUT, MIPERFIL...?!!


'''#rompe en perfil.save()NO LE SACO LA FICHA. 
#intento crear una vista de registro q junte ambos forms!, el UserRegisterForm y el PerfilForm!:
@login_required #podria no tenerlo xq desde aca tmb podria crear un nuevo usuario...creo. 
def registerPerfil(request): #en realidad es mas un editPerfil........
    usuario=request.user
    if request.method == 'POST': 
        form = UserEditForm(request.POST, instance=usuario) #el q uso para editarUsuario, model User.
        perfil_form = PerfilForm(request.POST) #el q uso para el crear, model Perfil
        if form.is_valid() and perfil_form.is_valid(): 
            informacion=form.cleaned_data
            info_perfil=perfil_form.cleaned_data
            usuario.username=informacion['username']
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save() #guardo el de User primero! o es usuario=form.save()?
        #ahora linkeo el campo user, q es el OneToOne:
            #perfil = perfil_form.save(commit=False) #????
            descripcion=info_perfil['descripcion']
            link= info_perfil['link']
            imagen= info_perfil['imagen']
            perfil=Perfil( user=usuario , imagen=imagen, descripcion=descripcion, link=link)  
            perfil.save() # ROMPE ACA!! xq???
            return render(request, 'accounts/registerPerfil.html', {'form':form, 'perfil_form':perfil_form,'mensaje':'TU PERFIL HA SIDO ACTUALIZADO'})
    else:
        form=UserEditForm() 
        perfil_form=PerfilForm() 
    
    return render(request, 'accounts/registerPerfil.html', {'form': form, 'perfil_form': perfil_form}) # o lo mando a otro lade q /profile??'''



