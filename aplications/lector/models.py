from django.db import models
from aplications.libro.models import Libro
# Create your models here.
class Lector(models.Model):
    nombre = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 30)
    nacionalidad = models.CharField(max_length = 30)
    edad   =models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE,related_name='libros_prestamo')
    
    fecha_prestamo  = models.DateField()
    fecha_devolucion  = models.DateField(blank=True,null=True)
    devuelto=models.BooleanField()

    def __str__(self):
        return self.libro.titulo


    