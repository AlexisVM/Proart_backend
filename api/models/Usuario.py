from django.contrib.auth.models import AbstractBaseUser,UserManager,PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

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
		return self._create_user(email, password, **extra_fields)
	def get_by_natural_key(self, email):
		return self.get(**{self.model.USERNAME_FIELD: email})


class Persona(models.Model):
	
	SEXOS = [
	('M', 'Masculino'),
	('F', 'Femenino'),
	('O', 'Otro'),
	]
	
	TIPO_PERSONA = [
	('A','Alumno'),
	('P','Profesor')
	]

	nombre = models.CharField(max_length=50,blank=True,null=True)
	apellido_materno = models.CharField(max_length=50,blank=True,null=True)
	apellido_paterno = models.CharField(max_length=50,blank=True,null=True)
	cumpleanos = models.DateField(blank=True,null=True)
	sexo = models.CharField(max_length=2, choices=SEXOS,blank=True,null=True,default='O')
	tipo_persona = models.CharField(max_length=2, choices=TIPO_PERSONA,blank=True,null=True,default='A')
	personas = models.ForeignKey('Usuario',related_name="personas_usuario",null=True,blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre

class Usuario(AbstractBaseUser, PermissionsMixin, Persona):
	
	TIPOCUENTA = [
	('I','Individual'),
	('G','Grupal'),
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

	
	email = models.EmailField(_('email address'), blank=False,unique=True)
	telefono=models.CharField(max_length=50,blank=True,null=True)
	calle=models.CharField(max_length=50,blank=True,null=True)
	pais=models.CharField(max_length=50,blank=True,null=True)
	estado=models.CharField(max_length=50,blank=True,null=True)
	numero=models.CharField(max_length=50,blank=True,null=True)
	colonia=models.CharField(max_length=50,blank=True,null=True)
	codigo_postal=models.CharField(max_length=50,blank=True,null=True)
	alergia=models.TextField(max_length=100,blank=True,null=True)
	tipo_de_sangre = models.CharField(max_length=3, choices=TIPOSANGRE,blank=True,null=True)
	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
	)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. '
			'Unselect this instead of deleting accounts.'
		),
	)
	tipo_de_cuenta = models.CharField(max_length=16, choices=TIPOCUENTA, default='I')
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nombre','apellido_paterno','apellido_materno','cumpleanos','sexo','password'] 
	objects  = UsuarioManager()

	def clean(self):
		super().clean()
		self.email = self.__class__.objects.normalize_email(self.email)

	def get_full_name(self):
		"""
		Return the first_name plus the last_name, with a space in between.
		"""
		full_name = '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)
		return full_name.strip()

	def get_short_name(self):
		"""Return the short name for the user."""
		return self.nombre

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""Send an email to this user."""
		send_mail(subject, message, from_email, [self.email], **kwargs)

