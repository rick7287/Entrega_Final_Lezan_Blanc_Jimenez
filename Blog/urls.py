from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', redirect_view, name='redirect_view'),
    path('pages/', paginas_ver, name='pages'),
    path('pagina_crear/', pagina_crear, name='pagina_crear'),
    path('pagina_borrar/<pagina_id>', pagina_borrar, name='pagina_borrar'),
    path('pagina_editar/<pagina_id>', pagina_editar, name='pagina_editar'),
    path('pages/<pagina_id>', pagina_detalle, name='pagina_detalle'),


]