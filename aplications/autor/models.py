from django.db import models


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 100)
    nacionalidad = models.CharField(max_length = 30)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)+'-'+self.nombre+'-'+self.apellidos
    
    def get_autor(self):
        out={
            "nombre":self.nombre,
            "apellido":self.apellidos,
            "nacionalidad":self.nacionalidad,
            "edad":self.edad
        }
        return out
    
    
    def get_autor2(self):
        out={
            "id":self.id,
            "nombre":self.nombre,
            "apellido":self.apellidos,
            "nacionalidad":self.nacionalidad,
            "edad":self.edad
        }
        return out
    
    