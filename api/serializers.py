from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from djoser import utils
from djoser.serializers import UserCreateSerializer
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from .models import *

##Get the current User Class defined in setting.py
User = get_user_model()


class UserCreateSerializerCustomFields(UserCreateSerializer):

	class Meta:
		model = User
		fields =  (
			settings.LOGIN_FIELD,
			"password",
			'nombre',
			'apellido_materno',
			'apellido_paterno',
			'cumpleanos',
			'sexo',
			'telefono',
			'pais',
			'estado',
			'colonia',
			'calle',
			'numero',
			'codigo_postal',
			'alergia',
			'tipo_de_sangre',
		)

