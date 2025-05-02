from django.db import models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    ESTADO_CHOICES = [
        ('leido', 'Leído'),
        ('quiero_leer', 'Quiero leer'),
        ('abandonado', 'Abandonado'),
    ]

    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    paginas = models.IntegerField(blank=True, null=True)
    año_publicacion = models.IntegerField(blank=True, null=True)
    formato = models.CharField(
        max_length=50,
        choices=[('ebook', 'Ebook'), ('blanda', 'Tapa blanda'), ('dura', 'Tapa dura'), ('audiolibro', 'Audiolibro')],
        default='ebook',
        blank=True,
        null=True
    )
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    calificacion = models.IntegerField(
        choices=[(i, f"{'⭐' * i}") for i in range(1, 6)],
        blank=True,
        null=True
    )
    notas = models.TextField(blank=True, null=True)
    citas = models.TextField(blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='leido')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return f"{self.titulo} – {self.autor}"