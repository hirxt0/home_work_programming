from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.CharField(max_length=30)
    url = models.URLField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Personage(models.Model):
    name = models.CharField(max_length=20)
    birth_year = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    mass = models.CharField(max_length=20)
    films = models.ManyToManyField(Movie, related_name='characters', blank=True)
    starships = models.ManyToManyField('Starship', related_name='members', blank=True)
    url = models.URLField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Starship(models.Model):
    name = models.CharField(max_length=40)
    max_atmosphering_speed = models.CharField(max_length=20)
    films = models.ManyToManyField(Movie, related_name='starships', blank=True)
    url = models.URLField(unique=True, blank=True, null=True)
    pilots = models.ManyToManyField(Personage, related_name='piloted_starships', blank=True)

    def __str__(self):
        return self.name
