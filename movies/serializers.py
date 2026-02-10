from rest_framework import serializers
from .models import Director, Pelicula


class DirectorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'nombre']


class PeliculaSerializer(serializers.ModelSerializer):
    # Para MOSTRAR el director con nombre
    director = DirectorMiniSerializer(read_only=True)

    # Para CREAR / EDITAR usando el ID
    director_id = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(),
        source='director',
        write_only=True
    )

    class Meta:
        model = Pelicula
        fields = [
            'id',
            'titulo',
            'genero',
            'fecha_estreno',
            'duracion_min',
            'poster',
            'director',     # lectura (nombre)
            'director_id'   # escritura (id)
        ]


class DirectorSerializer(serializers.ModelSerializer):
    peliculas = PeliculaSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = [
            'id',
            'nombre',
            'nacionalidad',
            'descripcion',
            'foto',
            'peliculas'
        ]
