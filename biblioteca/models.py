from django.db import models

class Livro(models.Model):
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    editora = models.CharField(max_length=200)


def __str__(self):
    return self.titulo
