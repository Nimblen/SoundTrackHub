from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.




class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    year = models.PositiveSmallIntegerField(validators=[
            MinValueValidator(1900),
            MaxValueValidator(timezone.now().year)
        ])
    film_url = models.URLField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
    


class FilmPhotos(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.film.name
    


class SoundTrack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    films = models.ManyToManyField(Film)
    track_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    