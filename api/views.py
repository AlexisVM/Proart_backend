from django.shortcuts import render
from djoser import views
from rest_framework.response import Response
from rest_framework import status, viewsets
from . import serializers
from .models import Programa

# Create yourfrom djoser import views views here.

class UsuarioViewSet(views.UserViewSet):
	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True,  fields=('email',))
		
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		#Bug if data = serializer.data
		return Response({'status':'created'}, status=status.HTTP_201_CREATED, headers=headers)

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data)

class TipoDeProgramasViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.TipoProgramaSerializer
	queryset = Programa.TipoPrograma.objects.all()
