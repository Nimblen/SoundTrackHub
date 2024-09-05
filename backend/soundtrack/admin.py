from django.contrib import admin
from django.utils.html import mark_safe 

from soundtrack.models  import  Genre, Film, FilmPhotos, SoundTrack
# Register your models here.




@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class FilmPhotosInline(admin.TabularInline):
    model = FilmPhotos
    extra = 1


@admin.register(FilmPhotos)
class FilmPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'photo')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'year', 'get_first_photo')
    filter_horizontal = ('genre',) 
    inlines = [FilmPhotosInline]

    def get_first_photo(self, obj):
        first_photo = obj.photos.first()  
        if first_photo and first_photo.photo:
            return mark_safe(f'<img src="{first_photo.photo.url}" width="100" height="100" />')
        return "No Photo"

    get_first_photo.short_description = "First Photo"


@admin.register(SoundTrack)
class SoundTrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
