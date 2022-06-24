from django.shortcuts import render, redirect
from django.http import HttpResponse
# Se importa el modelo para poder manipularlo desde el los render
from .models import Libro
#Se importa el modelo desde el archivo forms.py
from .forms import LibroForm


#Notas

"""
    -Un "Render" se utiliza para poder mostrar un archivo html
    -Un HttpResponse se utiliza solo para mostrar un valor html dentro del parentesis

"""

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    #Aqui se atraen todos los objetos de la clase libro para poder mostrarlos en el html
    libros = Libro.objects.all
    #                                               ↓↓↓ Esta variable es la que se lee en el index.html en el for
    return render(request, 'libros/index.html', {'libros': libros})

def crearLibro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    #Aqui se guardan los datos y se redireciona a libros
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    #                                               ↓↓↓ Esta variable es la que se lee en el form.html en el for
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editarLibro(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')