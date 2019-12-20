from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models

class UsuarioManager(UserManager):
	def _create_user(self, email, password, **extra_fields):
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(username, email, password, **extra_fields)


class Usuario(AbstractUser):
	SEXOS = [
	('M', 'Masculino'),
	('F', 'Femenino'),
	]
	TIPOSANGRE = [
	('O-', 'O negativo'),
	('O+', 'O positivo'),
	('A-', 'A negativo'),
	('A+', 'A positivo'),
	('B-', 'B negativo'),
	('B+', 'B positivo'),
	('AB-', 'AB negativo'),
	('AB+', 'AB positivo'),
	]
	nombre = models.CharField(max_length=50,blank=True,null=True)
	apellido_materno = models.CharField(max_length=50,blank=True,null=True)
	apellido_paterno = models.CharField(max_length=50,blank=True,null=True)
	email = models.CharField(max_length=50,blank=True,null=True,unique=True)
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
	tipo_de_sangre = models.CharField(max_length=3, choices=TIPOSANGRE,blank=True,null=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nombre','sexo','password'] 
	objects  = UsuarioManager()
	def __str__(self):
		return self.nombre