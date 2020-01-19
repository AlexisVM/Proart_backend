from django.shortcuts import render
from djoser import views
from rest_framework.response import Response

# Create yourfrom djoser import views views here.

class UsuarioViewSet(views.UserViewSet):
	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)
		
		for user in serializer.data:
			user.pop("persona_ptr")

		return Response(serializer.data)