from django.contrib import admin

#Se importa el modelo creado en models
from .models import Libro

#Para poder mani\pular los libros desde el administrador
admin.site.register(Libro)