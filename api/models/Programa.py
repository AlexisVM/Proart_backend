from django.db import models
from . import Usuario,fields
from ..validators import *
from ..utils import hashImage

class Disciplina(models.Model):
	nombre = models.CharField(max_length=30)
	def __str__(self):
		return self.nombre

class SubDisciplina(models.Model):
	nombre = models.CharField(max_length=30)
	disciplina_id = models.ForeignKey(Disciplina,
		null=True,
		on_delete=models.SET_NULL, 
		related_name = "subdisciplinas"
		)
	def __str__(self):
		return self.nombre


class TipoPrograma(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=100,blank=True)
	def __str__(self):
		return self.nombre

class Programa(models.Model):
	nombre = models.CharField(max_length=30)
	disciplinas = models.ManyToManyField(Disciplina)
	tipo_programa = models.ForeignKey(TipoPrograma,null=True,on_delete=models.SET_NULL)
	def __str__(self):
		return self.nombre


class Nivel(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=100,blank=True)
	dirigido = models.TextField(max_length=30)
	estructura = models.TextField(max_length=30)
	clase_derecho = models.PositiveSmallIntegerField()
	programa = models.ForeignKey('Programa',null=True,on_delete=models.SET_NULL, related_name="niveles")
	modalidad_semanal = models.TextField(max_length=30)
	edad_minima = models.PositiveSmallIntegerField()
	edad_maxima = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.nombre

class Semana(models.Model):
	fecha_inicio = models.DateField()
	fecha_final =  models.DateField()

class Bloque(models.Model):
	nivel = models.ForeignKey(Nivel,null=True,on_delete=models.SET_NULL, related_name="bloques")
	precio = models.PositiveSmallIntegerField()
	nombre = models.CharField(max_length=30)
	inicio = models.TimeField()
	final = models.TimeField()




class Grupo(models.Model):
	programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
	maestro = models.ManyToManyField(Usuario.Persona, related_name="maestros")
	nivel = models.ForeignKey(Nivel,on_delete=models.SET_NULL, null=True, related_name='grupos')
	semana = models.ForeignKey(Semana,on_delete=models.SET_NULL, null=True, related_name='grupos')
	inicio = models.TimeField()
	final = models.TimeField()
	bloque = models.ForeignKey(Bloque, on_delete=models.SET_NULL, null=True)
	dias = fields.DayOfTheWeekField()
	cupo = models.PositiveSmallIntegerField(default=20)

class Paquete(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=30)
	semanas = models.PositiveSmallIntegerField()

class Inscripcion(models.Model):
	PARCIALIDADES = [
	(1,'Una exhibición'),
	(3,'Tres pagos')
	]
	persona = models.ForeignKey(Usuario.Persona, on_delete=models.CASCADE, related_name="inscripciones")
	paquete = models.ForeignKey(Paquete, on_delete=models.SET_NULL, null=True)
	nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True)
	grupos = models.ManyToManyField(Grupo)
	programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
	parcialidades = models.PositiveSmallIntegerField(choices=PARCIALIDADES)

class Comprobante(models.Model):
	TIPO_PAGO = [('D','Depósito'),
	('T','Transferencia'),
	('E','Efectivo'),
	]
	inscripcion = models.ForeignKey(Inscripcion,on_delete=models.SET_NULL, null=True)
	archivo = models.FileField(upload_to=hashImage, validators=[validate_comprobante])
	fecha_de_subida = models.DateField(blank=True,null=True)
	fecha_limite = models.DateField(blank=True,null=True)
	monto = models.DecimalField(max_digits=5, decimal_places=2)
	aprobado = models.BooleanField(default=False)
	parcialidad = models.PositiveSmallIntegerField()
	tipo_de_pago = models.CharField(max_length=3, choices=TIPO_PAGO, default='D')