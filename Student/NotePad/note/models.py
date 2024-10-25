from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'{self.pk}. {self.title} by {self.author}'

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}. {self.name}: {self.description} {self.image}'