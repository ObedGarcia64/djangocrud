from django.urls import path
from . import views

#Se importa las configuraciones y ademas se importan los archivos estaticos para poder mostrar las imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static

#Es importante verificar que el nombre despues de views coincida con el nombre agregado en el archivo views.py
"""Como segundo dato es que el nombre despues de name="" es el que se estara utilizando en los archivos 
    html (Conocimiento de hasta ahora si hay otro lugar en el que se puedan utilizar lo agregare despues)"""
urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('crear', views.crearLibro, name='crear'),
    path('editar', views.editarLibro, name='editar'),

    #Se le agrega el id para saber que libro se va a eliminar
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/editar/<int:id>', views.editarLibro, name='editar')

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Para poder mostrar las imagnes importando la configuracion de los settings 