from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('libro/<int:libro_id>/', views.libro_detalle, name='libro_detalle'),
    path("ver-log/", views.ver_log),
]    