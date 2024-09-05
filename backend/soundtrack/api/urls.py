from rest_framework.routers import DefaultRouter 

from .viewsets import FilmModelViewSet, SoundTrackModelViewSet, GenreModelViewSet, FilmPhotosModelViewSet




router = DefaultRouter()
router.register(r'genre', GenreModelViewSet)
router.register(r'films-photos', FilmPhotosModelViewSet)
router.register(r'films', FilmModelViewSet)
router.register(r'soundtracks', SoundTrackModelViewSet)




urlpatterns = []
urlpatterns += router.urls
