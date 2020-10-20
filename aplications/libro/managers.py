import datetime
from django.db import models
#from django.db.models import Q

class LibroManager(models.Manager):
    """ manager para el modelo autor """

    # def listar_libros(self):
    #     return self.all()
    
    def filtrar_fecha_entre(self):
        resultado=self.filter(
            fecha__range=('1980-09-09','2010-09-09')
        )
        return resultado
    
    def buscar_libros(self,kword,fecha1,fecha2):
        #transformando las fechas a tipo date
        date1=datetime.datetime.strptime(fecha1,"%Y-%m-%d").date()
        date2=datetime.datetime.strptime(fecha2,"%Y-%m-%d").date()
        resultado=self.filter(
            titulo__icontains=kword,
            fecha__range=(date1,date2)
        )
        return resultado

    def listar_libros_categoria(self,categoria):
        resultado=self.filter(categoria_id=categoria).order_by('titulo')
        return resultado

class CategoriaManager(models.Manager):
    """manager para el modelos autor"""
   
    def categoria_por_autor(self,autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()