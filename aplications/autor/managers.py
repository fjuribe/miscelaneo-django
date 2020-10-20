from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """ manager para el modelo autor """

    def listar_autores(self):
        return self.all()
    
    def buscar_autor(self,kword):
        resultado=self.filter(nombre=kword)
        return resultado
    
    def buscar_autor2(self,kword):
        resultado=self.filter(Q(nombre=kword) | Q(apellidos=kword))
        return resultado
    
    def buscar_autor3(self,kword):
        resultado=self.filter(Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)).exclude(Q(edad=65))
        return resultado

    #mayor a 40 y edad  menor que 65
    def buscar_autor4(self,kword):
        resultado=self.filter(edad__gt=40,edad__lt=80).order_by('apellidos','nombre')
        return resultado

