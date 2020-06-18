from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.genre)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) 