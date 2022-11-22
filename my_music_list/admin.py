from django.contrib import admin
from .models import *

# admin.site.register(Band)
# admin.site.register(Album)
# admin.site.register(Song)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Label)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    list_filter = ('title',)


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('title', 'website', 'genre_display')
    filter_horizontal = ['genre', 'label']
    list_filter = ('title', 'website',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'album')
