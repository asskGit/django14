from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    year = models.IntegerField(default=0)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    director = models.CharField(max_length=100)
    time = models.TimeField()
    rating = models.IntegerField(default=0)
    age = models.IntegerField(default=16)
    operator = models.CharField(max_length=100)

    def __str__(self):
        return self.title



