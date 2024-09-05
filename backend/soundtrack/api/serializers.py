from rest_framework import serializers


from soundtrack.models import Genre, Film, SoundTrack, FilmPhotos




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']




class FilmPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPhotos
        fields = ['id', 'film', 'photo']

class FilmSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, queryset=Genre.objects.all(), slug_field='name')
    photos = FilmPhotosSerializer(many=True) 

    class Meta:
        model = Film
        fields = ['id', 'name', 'description', 'year', 'film_url', 'genre', 'photos']

class SoundTrackSerializer(serializers.ModelSerializer):
    film = FilmSerializer(many=True)
    class Meta:
        model = SoundTrack
        fields = ['id', 'name', 'description', 'film', 'track_url']


