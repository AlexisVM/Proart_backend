from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from djoser import utils
from djoser.serializers import UserCreateSerializer,UserSerializer
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from .models import *
from rest_framework.utils.serializer_helpers import ReturnDict

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
		fields = ('email','password','nombre','apellido_paterno','apellido_materno','cumpleanos','sexo','tipo_de_cuenta')
