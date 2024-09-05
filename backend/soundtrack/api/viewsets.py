from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    FilmSerializer,
    SoundTrackSerializer,
    GenreSerializer,
    FilmPhotosSerializer,
)
from soundtrack.models import Film, SoundTrack, Genre, FilmPhotos


class GenreModelViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAdminUser]


class FilmPhotosModelViewSet(viewsets.ModelViewSet):
    queryset = FilmPhotos.objects.all()
    serializer_class = FilmPhotosSerializer
    permission_classes = [permissions.IsAdminUser]


class FilmModelViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filterset_fields = ["genre", "year"]
    search_fields = ["name", "genre__name"]
    ordering_fields = ["name", "year"]
    ordering = ["year"]


class SoundTrackModelViewSet(viewsets.ModelViewSet):
    queryset = SoundTrack.objects.all()
    serializer_class = SoundTrackSerializer
    filterset_fields = ["films"]
