from django.db import models

class Livro(models.Model):
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    editora = models.CharField(max_length=200)

    def publish(self):
        self.save()


    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    cliente = models.CharField(max_length=200)
    livro = models.CharField(max_length=200)

    def publish(self):
        self.save()


    def __str__(self):
        return self.cliente
