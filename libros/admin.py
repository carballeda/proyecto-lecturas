from django.contrib import admin
from .models import Libro, Etiqueta
from .forms import LibroForm

class LibroAdmin(admin.ModelAdmin):
    form = LibroForm
    list_display = ['titulo', 'autor', 'calificacion', 'fecha_fin', 'estado']
    list_filter = ['estado', 'calificacion', 'genero', 'fecha_fin', 'formato']  # Filtros en el panel de administración
    ordering = ['-fecha_fin']  # Ordenar por fecha de fin, más reciente primero
    search_fields = ['titulo', 'autor']  # Permite buscar por título o autor
    exclude = ['portada']  # xcluimos el campo que da problemas en Render

admin.site.register(Libro, LibroAdmin)
admin.site.register(Etiqueta)