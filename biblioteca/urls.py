from django.urls import path, include
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),
    path('categorias/<int:id>/', views.libros_por_categoria, name='libros_por_categoria'),
]