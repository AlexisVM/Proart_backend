from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
	SEXOS = [
	('M', 'Masculino'),
	('F', 'Femenino'),
	]
	nombre = models.CharField(max_length=50,blank=True,null=True)
	apellido_materno = models.CharField(max_length=50,blank=True,null=True)
	apellido_paterno = models.CharField(max_length=50,blank=True,null=True)
	cumpleanos = models.DateField(blank=True,null=True)
	sexo = models.CharField(max_length=2, choices=SEXOS,blank=True,null=True)
	telefono=models.CharField(max_length=50,blank=True,null=True)
	calle=models.CharField(max_length=50,blank=True,null=True)
	pais=models.CharField(max_length=50,blank=True,null=True)
	estado=models.CharField(max_length=50,blank=True,null=True)
	numero=models.CharField(max_length=50,blank=True,null=True)
	colonia=models.CharField(max_length=50,blank=True,null=True)
	codigo_postal=models.CharField(max_length=50,blank=True,null=True)
	alergia=models.TextField(max_length=100,blank=True,null=True)

	def __str__(self):
		return self.username