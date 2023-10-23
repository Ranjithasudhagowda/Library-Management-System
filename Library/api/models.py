from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=255)

    class Meta:
        app_label = 'api'
