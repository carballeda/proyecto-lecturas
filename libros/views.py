from django.shortcuts import render
from .models import Libro
from django.db.models import Q

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

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_test(request):
    return Response({"status": "ok", "message": "La API funciona"})