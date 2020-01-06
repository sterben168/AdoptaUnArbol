from django.shortcuts import render

# Create your views here.

from .models import Arbol, Persona
from django.views import generic


def index(request):
	"""
	Función vista para la página inicio del sitio.
	"""
	# Genera contadores de Arboles y Personas
	num_arboles=Arbol.objects.all().count()
	num_personas=Persona.objects.all().count()  # El 'all()' esta implícito por defecto.
	
	# Renderiza la plantilla HTML index.html con los datos en la variable contexto
	return render(
	    request,
	    'index.html',
	    context={'num_arboles':num_arboles,'num_personas':num_personas},
	)

#nos permite tener una lista de arboles
class VistaArboles(generic.ListView):
    model = Arbol 

#nos permite ver los detalles de cada objeto arbol 
class DetallesArboles(generic.DetailView):
    model = Arbol 


#nos permite tener una lista de personas 
class VistaPersonas(generic.ListView):
    model = Persona 

#nos permite ver los detalles de cada objeto persona 
class DetallesPersonas(generic.DetailView):
    model = Persona 
