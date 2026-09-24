from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    
    contexto = {
        'libros': libros,
        'categorias': [c[0] for c in Libro.CATEGORIAS],
        'disponibles': [libro for libro in libros if libro.disponible],
        'total_libros': libros.count()
    }

    return render(request, 'lista_libros.html', contexto)


def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    contexto = {
        'libro': libro
    }
    return render(request, 'detalle_libro.html', contexto)

def libros_por_categoria(request, cat):
    libros = Libro.objects.filter(categoria=cat)
    contexto = {
        'libros': libros,
        'categoria': cat,
        'total_libros': libros.count()
    }
    return render(request, 'libros_por_categoria.html', contexto)

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()

    contexto = {
        'form': form
    }
    return render(request, 'agregar_libro.html', contexto)
