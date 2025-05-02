# libros/management/commands/importar_lecturas.py

import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from libros.models import Libro

class Command(BaseCommand):
    help = 'Importa lecturas desde un archivo CSV exportado de Goodreads'

    def handle(self, *args, **options):
        with open(r"C:\Users\Greta\OneDrive\_Python\proyecto_BBDD\archivo_importar_gr.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convertir la fecha de lectura
                fecha_str = row['Fecha fin']
                fecha_fin = datetime.strptime(fecha_str, '%d/%m/%Y').date() if fecha_str else None

                # Buscar el libro por título y autor
                libro, created = Libro.objects.update_or_create(
                    titulo=row['Titulo'],
                    autor=row['Autor'],
                    defaults={
                        'isbn': row['ISBN'] or None,
                        'calificacion': int(row['Calificacion']) if row['Calificacion'] else None,
                        'paginas': int(row['Paginas']) if row['Paginas'] else None,
                        'fecha_fin': fecha_fin,
                        'formato': 'ebook',  # Rellena por defecto todos los libros con "ebook"
                        'notas': '',  # Cambia esto si tienes un campo de notas
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Importado: {libro.titulo}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Reescrito: {libro.titulo}'))
