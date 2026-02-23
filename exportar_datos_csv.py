import os
import django
import csv

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lecturas.settings")  
django.setup()

# Importa tu modelo
from libros.models import Libro

# Crea el CSV
with open("libros.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Cabecera
    writer.writerow([
        "id",
        "titulo",
        "autor",
        "paginas",
        "año_publicacion",
        "formato",
        "fecha_inicio",
        "fecha_fin",
        "calificacion",
        "genero",
        "estado",
    ])

    # Filas
    for libro in Libro.objects.all():
        writer.writerow([
            libro.id,
            libro.titulo,
            libro.autor,
            libro.paginas,
            libro.año_publicacion,
            libro.formato,
            libro.fecha_inicio,
            libro.fecha_fin,
            libro.calificacion,
            libro.genero,
            libro.estado,
        ])

print("CSV creado correctamente: libros.csv")