from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Label(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title or ''


class Band(models.Model):
    title = models.CharField(max_length=55)
    website = models.CharField(max_length=55)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='bands')
    genre = models.ManyToManyField(Genre, blank=True)
    label = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.title or ''

    #def country_display(self):
        #return ', '.join([country.title for country in self.country.all()])

    #country_display.short_description = "Country"

    def genre_display(self):
        return ', '.join([genre.title for genre in self.genre.all()])

    genre_display.short_description = "Genre"


class Album(models.Model):
    title = models.CharField(max_length=55, verbose_name='album', blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True)
    created_by = models.ForeignKey(Band, on_delete=models.CASCADE, verbose_name='band', related_name='albums')

    def __str__(self):
        return self.title or ''




class Song(models.Model):
    title = models.CharField(max_length=55, verbose_name='song')
    durations = models.IntegerField(blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title
