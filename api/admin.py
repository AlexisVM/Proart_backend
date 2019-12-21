from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.translation import gettext, gettext_lazy as _
from dateutil.relativedelta import relativedelta
import datetime

##Custom Admins
class UsuarioAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('nombre','apellido_paterno', 'apellido_materno','cumpleanos','sexo','telefono','pais','estado','colonia','calle','numero','codigo_postal')}),
		(_('Permissions'), {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
		)
	list_display = ('nombre','apellido_paterno', 'apellido_materno','email','edad','sexo', 'is_staff')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
	search_fields = ('nombre','apellido_paterno', 'apellido_materno', 'email','sexo')
	ordering = ('apellido_paterno','apellido_materno')
	filter_horizontal = ('groups', 'user_permissions',)
	
	def edad(self, obj):
		return ("%s" % relativedelta(datetime.date.today(),obj.cumpleanos).years)


admin.site.register(Usuario.Usuario, UsuarioAdmin)
admin.site.register(Programa.Disciplina)
admin.site.register(Programa.SubDisciplina)
admin.site.register(Programa.TipoPrograma)
admin.site.register(Programa.Nivel)
admin.site.register(Programa.Programa)