from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=60, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    # NUEVO: foto en Base64
    foto = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='peliculas'
    )
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=50, blank=True)
    fecha_estreno = models.DateField(null=True, blank=True)
    duracion_min = models.PositiveIntegerField(null=True, blank=True)

    # NUEVO: poster en Base64
    poster = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
