from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 100)
    genero = models.CharField(max_length = 30)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)+'-'+self.nombre+'-'+self.apellidos
    
    def get_persona(self):
        out={
            "nombre":self.nombre,
            "apellido":self.apellidos,
            "genero":self.genero,
            "edad":self.edad
        }
        return out
    