from django.urls import path
from AppEntrega1.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('vino/', vino, name= 'vino'),
    path('bodega/', bodega, name= 'bodega'),
    path('cliente/', cliente, name= 'cliente'),
    path('bodegaFormulario/', bodegaFormulario, name= 'bodegaFormulario'),
    path('vinoFormulario/', vinoFormulario, name= 'vinoFormulario'),
    path('clienteFormulario/', clienteFormulario, name= 'clienteFormulario'),
    path('busquedaCliente/', busquedaCliente, name= 'busquedaCliente'),
    path('buscar/', buscar, name= 'buscar'),
]