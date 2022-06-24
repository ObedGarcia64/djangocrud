from distutils.command.upload import upload
from django.db import models

#Las clases creadas aqui como por ejemplo esta ↓↓↓ seran las que manejen las bases de datos
#Para que se incorporen es necesario correr los comandos "py manage.py makemigrations" y "py manage.py migrate"

class Libro(models.Model):
    id                  = models.AutoField(primary_key=True)
    # Cabe destacara aqui que el verbose_name, es el nombre que aparecera cuando lo agregemos en el forms.html en el campo.label
    titulo              = models.CharField(max_length=100, verbose_name="Titulo")
    #                                                      ↓↓ LA carpeta imagenes se crea sola al crear el primer registro
    imagen              = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    descripcion         = models.TextField(verbose_name="Descripcion", null=True)

    #Con este def, definimos lo que se estara mostrando en las listas del administrador 
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila

    #Este campo es para que pueda desaparecer la imagen cuando se elimina un libro de la base de datos desde el administrador
    def delete(self, using=None, keep_parents=False):
        #                                 ↓↓ este es el nombre que se le dio a la imagen desde la clase
        self.imagen.storage.delete(self.imagen.name)
        super().delete()