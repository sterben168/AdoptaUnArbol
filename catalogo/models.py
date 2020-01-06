from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Arbol(models.Model):
	"""
	Modelo que representa los arboles adoptados 
	"""

	#id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este arbol en todo el catalogo")	

	#Especie de arbol
	especie = models.CharField(max_length=200) 

	#Persona que adopto el arbol
	persona = models.ForeignKey('Persona', on_delete=models.SET_NULL, null=True)

	#Localizacion del arbol
	localizacion = models.CharField(max_length=200, default="Rancho Quemado" )

	def __str__(self):
		"""
		String que representa al objeto Arbol con su especie y su id
		"""
		return '%s (%s)' % (self.especie, self.persona)

	def get_absolute_url(self):
	        """
	        Devuelve el URL a una instancia particular de Arbol
	        """
	        return reverse('detalles-arbol', args=[str(self.id)])


class Persona(models.Model):
	"""
	Modelo que representa los arboles adoptados 
	"""

	#Nombre de la persona que adopta el arbol
	nombre = models.CharField(max_length=100)
	
	#Apellidos de la persona que adopta el arbol
	apellidos = models.CharField(max_length=100)


	def __str__(self):
		"""
		String que representa al objeto Persona
		"""
		return '%s %s' % (self.nombre, self.apellidos)


	def get_absolute_url(self):
		"""
		Retorna la url para acceder a una instancia particular de una Persona.
		"""
		return reverse('detalles-persona', args=[str(self.id)])
