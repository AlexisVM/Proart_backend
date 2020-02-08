from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers, fields as f
from rest_framework.exceptions import ValidationError
from djoser import utils
from djoser.serializers import UserCreateSerializer,UserSerializer
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from .models import *
from rest_framework.utils.serializer_helpers import ReturnDict
from django.conf import settings as globalsettings
##Get the current User Class defined in setting.py
User = get_user_model()

class UserCreateSerializerCustomFields(UserCreateSerializer):
	def __init__(self, *args, **kwargs):
		fields = kwargs.pop('fields', None)
		super(UserCreateSerializerCustomFields, self).__init__(*args, **kwargs)
		if fields is not None:
			allowed = set(fields)
			existing = set(self.fields)
			for field_name in existing - allowed:
				self.fields.pop(field_name)


	class Meta:
		model = User
		#print(User._meta.get_fields(include_hidden=True))
		read_only_fields = ('persona_ptr',)
		fields = ('email','password','nombre','apellido_paterno','apellido_materno','cumpleanos','sexo','tipo_de_cuenta')

class DynamicUserSerializer(UserSerializer):
	def __init__(self, *args, **kwargs):
		fields = kwargs.pop('fields', None)
		super(DynamicUserSerializer, self).__init__(*args, **kwargs)
		if fields is not None:
			allowed = set(fields)
			existing = set(self.fields)
			for field_name in existing - allowed:
				self.fields.pop(field_name)
	class Meta:
		model = User
		fields = ('email','nombre','apellido_paterno','apellido_materno',)

class TipoProgramaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Programa.TipoPrograma
		fields = ['id','nombre','descripcion']

class SubDisciplinasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Programa.SubDisciplina
		fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
	subdisciplinas = SubDisciplinasSerializer(many=True)
	class Meta:
		model = Programa.Disciplina
		fields = ('id','nombre','subdisciplinas')

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario.Persona
		fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
	maestro = PersonaSerializer(many=True)
	dias = f.MultipleChoiceField(choices=fields.DAY_OF_THE_WEEK)
	class Meta:
		model = Programa.Grupo
		fields = ('id','dias','inicio','final','cupo','fecha_inicio','fecha_final','maestro')

class NivelSerializer(serializers.ModelSerializer):
	grupos = GrupoSerializer(many=True)
	class Meta:
		model = Programa.Nivel
		fields = ('nombre','descripcion','clase_derecho','grupos','precio')

class ProgramaSerializer(serializers.ModelSerializer):
	disciplinas = DisciplinaSerializer(many=True)
	niveles = NivelSerializer(many=True)
	class Meta:
		model = Programa.Programa
		fields = ('id','nombre','dirigido','estructura','modalidad_semanal','edad_minima','edad_maxima','disciplinas','tipo_programa','disciplinas','niveles')

class UserMeSerializer(DynamicUserSerializer):
	class Meta:
		model = User
		fields = '__all__'
