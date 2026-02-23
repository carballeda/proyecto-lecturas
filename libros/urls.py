from django.urls import path
from . import views
from .views import api_test

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('libro/<int:libro_id>/', views.libro_detalle, name='libro_detalle'),
    path('api/test/', api_test),
]    