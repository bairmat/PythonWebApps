from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('author_list')


class Article (models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('article_list')
