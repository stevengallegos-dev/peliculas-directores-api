from rest_framework import serializers
from .models import Director, Pelicula

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    peliculas = PeliculaSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'nombre', 'nacionalidad', 'fecha_nacimiento', 'foto', 'peliculas']
