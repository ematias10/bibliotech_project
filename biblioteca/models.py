from django.db import models

class Libro(models.Model):
    CATEGORIAS = [
        ('TECNOLOGIA', 'Tecnología e Informática'),
        ('NARRATIVA', 'Narrativa y Literatura'),
        ('CIENCIA', 'Ciencias Exactas y Naturales'),
        ('HISTORIA', 'Historia y Ciencias Sociales'),
    ]

    isbn = models.CharField(max_length=20, unique=True, verbose_name="ISBN")
    titulo = models.CharField(max_length=150, verbose_name='Título del Libro')
    autor = models.CharField(max_length=100, verbose_name='Autor')
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, verbose_name='Categoría')
    precio_prestamo = models.IntegerField(verbose_name='Precio Préstamo ($ CLP)')
    stock_copias = models.IntegerField(verbose_name='Copias Disponibles')
    disponible = models.BooleanField(default=True, verbose_name='Disponible')
    fecha_publicacion = models.DateField(verbose_name='Fecha de Publicación')

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

