from rest_framework.routers import DefaultRouter
from .views import DirectorViewSet, PeliculaViewSet

router = DefaultRouter()
router.register(r'directores', DirectorViewSet)
router.register(r'peliculas', PeliculaViewSet)

urlpatterns = router.urls
