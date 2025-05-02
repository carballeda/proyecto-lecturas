from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['portada', 'titulo', 'autor', 'isbn', 'paginas', 'año_publicacion', 'formato', 'fecha_inicio', 'fecha_fin', 'calificacion', 'notas', 'citas', 'genero', 'estado', 'etiquetas']

    calificacion = forms.TypedChoiceField(
    choices=[(i, f"{'⭐' * i}") for i in range(1, 6)],
    widget=forms.RadioSelect(attrs={'class': 'rating'}),
    coerce=int,  # convierte el valor a int
    required=False,  # permite dejarlo en blanco
    empty_value=None  # qué valor usar si se deja vacío
)