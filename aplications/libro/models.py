from django.db import models
from aplications.autor.models import Autor
import json

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=30)
    def __str__(self):
        return str(self.id)+' - '+self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='categoria_libro')
    autores   = models.ManyToManyField(Autor)
    titulo    = models.CharField(max_length = 50)
    fecha     = models.DateField('fecha de lanzamiento')
    portada   = models.ImageField(upload_to='portada')
    visitas   =models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.id)+"-"+self.titulo

    def get_libro(self):
        lb={
            "titulo":self.titulo,
            "fecha":self.fecha,
            "visitas":self.visitas,
            "portada":json.dumps(str(self.portada))
        }
        return lb
    
    
    
    