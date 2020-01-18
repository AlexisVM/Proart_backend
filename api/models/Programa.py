from django.db import models

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
	disciplinas = models.ManyToManyField(SubDisciplina)
	nivel = models.ForeignKey(Nivel,null=True,on_delete=models.SET_NULL)
	tipo_programa = models.ForeignKey(TipoPrograma,null=True,on_delete=models.SET_NULL)

	def __str__(self):
		return self.nombre