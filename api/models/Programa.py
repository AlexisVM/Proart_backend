from django.db import models
from . import Usuario,fields
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

class Nivel(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=100,blank=True)
	clase_derecho = models.PositiveSmallIntegerField()
	programa = models.ForeignKey('Programa',null=True,on_delete=models.SET_NULL)
	def __str__(self):
		return self.nombre

class Programa(models.Model):
	nombre = models.CharField(max_length=30)
	dirgido = models.TextField(max_length=30)
	estructura = models.TextField(max_length=30)
	modalidad_semanal = models.TextField(max_length=30)
	edad_minima = models.PositiveSmallIntegerField()
	edad_maxima = models.PositiveSmallIntegerField()
	precio = models.PositiveSmallIntegerField()
	disciplinas = models.ManyToManyField(Disciplina)
	tipo_programa = models.ForeignKey(TipoPrograma,null=True,on_delete=models.SET_NULL)
	def __str__(self):
		return self.nombre



class Grupo(models.Model):
	programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
	maestro = models.ManyToManyField(Usuario.Persona)
	nivel = models.OneToOneField(Nivel,on_delete=models.SET_NULL, null=True)
	inicio = models.TimeField()
	final = models.TimeField()
	dias = fields.DayOfTheWeekField()

class Inscripcion(models.Model):
	PARCIALIDADES = [
	(1,'Una exhibición'),
	(3,'Tres pagos')
	]
	persona = models.ForeignKey(Usuario.Persona, on_delete=models.CASCADE)
	programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
	grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)
	parcialidades = models.PositiveSmallIntegerField(choices=PARCIALIDADES)

class Comprobante(models.Model):
	comprobante = models.ForeignKey(Inscripcion,on_delete=models.SET_NULL, null=True)
	archivo = models.FileField(upload_to='comprobantes')
	fecha_de_subida = models.DateField(blank=True,null=True)
	fecha_limite = models.DateField(blank=True,null=True)
	monto = models.DecimalField(max_digits=5, decimal_places=2)