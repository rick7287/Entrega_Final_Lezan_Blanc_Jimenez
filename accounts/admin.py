from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin #para poder manejar los perfiles desde admin
from django.contrib.auth.models import User
from .models import Perfil

# al final no estoy seguro si esto hacia falta...
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfil'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

#regitro mi modelo Perfil. no hace falta si ya hago todo lo de abajo??
admin.site.register(Perfil)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)