from django.shortcuts import render
from django.http import JsonResponse
from .models import Libro
from django.db.models import Q
from django.http import HttpResponse
import os

def libro_detalle(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    return render(request, 'libros/libro_detalle.html', {'libro': libro})

def lista_libros(request):
    query = request.GET.get('q')  
    libros = Libro.objects.all().order_by('-fecha_fin')

    if query:
        libros = libros.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query)
        )

    return render(request, 'libros/lista_libros.html', {'libros': libros, 'query': query})

# API de prueba simplificada (sin DRF)
def api_test(request):
    return JsonResponse({"status": "ok", "message": "La API funciona"})

# vista para comprobar logs en render
def ver_log(request):
    log_path = os.path.join(os.path.dirname(__file__), "../logs/errores_render.log")
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            contenido = f.read()
        return HttpResponse(f"<pre>{contenido}</pre>")
    return HttpResponse("No hay log todavía")