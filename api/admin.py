from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite,ModelAdmin
from django.db import models
from .models import *
import datetime
from .modeladmin import *

##Admin Site
class AdminSite(AdminSite):
	site_header = 'Ibérica'
	#login_template ='admin/login.html'
	#login_form = AuthForm


admin = AdminSite(name='Ibérica')





admin.register(Usuario.Usuario, UsuarioAdmin)
admin.register(Usuario.Persona)
admin.register(Programa.Disciplina)
admin.register(Programa.SubDisciplina)
admin.register(Programa.TipoPrograma)
admin.register(Programa.Nivel)
admin.register(Programa.Programa)
admin.register(Programa.Comprobante, ComprobanteAdmin)
admin.register(Programa.Inscripcion)
admin.register(Programa.Grupo,GrupoModelAdmin)
