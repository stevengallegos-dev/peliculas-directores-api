from django.contrib import admin
from .models import Director, Pelicula

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'director', 'genero')
    list_filter = ('genero', 'director')
    search_fields = ('titulo',)
