from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.translation import gettext, gettext_lazy as _

##Custom Admins
class UsuarioAdmin(UserAdmin):
	fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('nombre', 'apellido_paterno', 'apellido_materno','cumpleanos','sexo','telefono','pais','estado','colonia','calle','numero','codigo_postal')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )

admin.site.register(Usuario.Usuario, UsuarioAdmin)

