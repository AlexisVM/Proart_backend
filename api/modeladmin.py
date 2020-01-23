from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from dateutil.relativedelta import relativedelta
import datetime
from django.db import models
from .widgets import *
from .models.Usuario import Persona
##Custom Admins
class UsuarioAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('nombre','apellido_paterno','apellido_materno','cumpleanos','sexo','telefono','pais','estado','colonia','calle','numero','codigo_postal')}),
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
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)
	def edad(self, obj):
		return ("%s" % relativedelta(datetime.date.today(),obj.cumpleanos).years)

class ComprobanteAdmin(ModelAdmin):
	formfield_overrides = {
		models.FileField: {'widget': AdminImagePdfWidget},
		models.ImageField: {'widget': AdminImagePdfWidget},
	}
	list_display = ('aprobado','archivo')
	list_filter = ('aprobado',)

class GrupoModelAdmin(ModelAdmin):
	def formfield_for_manytomany(self, db_field, request, **kwargs):
		if db_field.name == "maestro":
			kwargs["queryset"] = Persona.objects.filter(tipo_persona='P')
		return super().formfield_for_manytomany(db_field, request, **kwargs)