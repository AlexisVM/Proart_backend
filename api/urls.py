"""proart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
	path('users/', UsuarioViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
    'put': 'update',
    'patch': 'partial_update'
    })), 
    path('me/', UsuarioViewSet.as_view({
    'get': 'me',
    'delete': 'me',
    'put': 'me',
    'patch': 'me',
    })),
    path('auth/login/', views.TokenCreateView.as_view()),
    path('auth/logout/', views.TokenDestroyView.as_view()),
    

    path('programas/', ProgramasViewSet.as_view({
        'get': 'list'
        })),
    path('grupos/', GruposViewSet.as_view({
        'get': 'list',
        })),
    path('paquetes/', PaqueteViewSet.as_view({
        'get': 'list',
        })),
    path('inscripciones/', InscripcionViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
    'put': 'update',
    'patch': 'partial_update'
    })), 
    ] 
