from django.db import models

# Create your models here.


class Productor(models.Model):
    nombre = models.CharField(max_length=100)
    precion = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()


def __str__(self):
    return self.nombre
