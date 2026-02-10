from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Director, Pelicula
from .serializers import DirectorSerializer, PeliculaSerializer


class ReadOnlyOrAuthenticated(viewsets.ModelViewSet):
    def get_permissions(self):
        # COMO tus vistas públicas: index(), lista_entrenadores()
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return [AllowAny()]
        # COMO tus vistas con @login_required: add/edit/delete
        return [IsAuthenticated()]


class DirectorViewSet(ReadOnlyOrAuthenticated):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class PeliculaViewSet(ReadOnlyOrAuthenticated):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
