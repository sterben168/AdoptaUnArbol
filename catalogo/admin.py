from django.contrib import admin

# Register your models here.

from .models import Arbol, Persona

#se registran los modelos arbol y persona
#para que se puedan utilizar en la página
#de administración
admin.site.register(Arbol)
admin.site.register(Persona)
