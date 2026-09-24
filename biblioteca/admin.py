from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria')
    search_fields = ('titulo', 'autor')
    list_filter = ('categoria', 'disponible')