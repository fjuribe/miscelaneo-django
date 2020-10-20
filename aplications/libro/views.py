from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from django.db.models import Q,Count,Avg
from .models import Libro,Categoria
from aplications.autor.models import Autor
from aplications.lector.models import Prestamo,Lector
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth.models import User
# from .permissions import StudentPermission

# Create your views here.
class AutorId_xlibro(APIView):
    def get(self,request,pk,format=None):
        lista_libros=[]
        autor=Autor.objects.get(id=pk)
        libros=Libro.objects.filter(autores__id=pk)
        author=autor.nombre+" "+autor.apellidos
        
        if len(libros)>0:
            for lb in libros:
                lib={"id":lb.id,"titulo":lb.titulo,"fecha":lb.fecha,"visitas":lb.visitas}
                lista_libros.append(lib)
            return HttpResponse(JsonResponse({"success":author,"libros":lista_libros}),content_type="application/json", status=200)
        else:
            return HttpResponse(JsonResponse({"autor":"No existe"}),content_type="application/json", status=404)
        
            
class ListarLibroPorCategoria(APIView):
    def get(self,format=None):
        lista_result=[]
        resultado=Categoria.objects.annotate(num_libros=Count('categoria_libro')).values()

        return HttpResponse(JsonResponse({"success":list(resultado)}),content_type="application/json", status=200)

class LibrosPrestados(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    def get(self,format=None):
        resultado=Libro.objects.aggregate(libros_prestados=Count('libros_prestamo'))
        return HttpResponse(JsonResponse({"success":resultado}),content_type="application/json", status=200)

class PromedioEdadesLectores(APIView):
    def get(self,format=None):
        resultado=Prestamo.objects.aggregate(promedio_edad=Avg('lector__edad'),numero_lectores=Count('lector__id'))
        return HttpResponse(JsonResponse({"success":resultado}),content_type="application/json", status=200)

# class NumLibrosPrestados():
#     def get(self,format=None):

class TipoDeUser(APIView):
    list=[]
    def get(self,request,format=None):
        usuario=request.get_group_permissions()
        print(usuario)
        return HttpResponse(JsonResponse({"success":set(usuario)}),content_type="application/json", status=200)


#############################################################################################################################

class BuscarTodosLosLibros(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    def get(self,format=None):
        lista=[]
        libros=Libro.objects.all()
        if len(libros)>0:
            for libro in libros:
                obj={"id":libro.id,"titulo":libro.titulo,"fecha":libro.fecha}
                lista.append(obj)
            return HttpResponse(JsonResponse({"libros":lista}),content_type="application/json", status=200)
        else:
            return HttpResponse(JsonResponse({"libros":"No existen libros"}),content_type="application/json", status=404) 

class BuscarLibroPorId(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,pk,format=None):
        try:
            libro=Libro.objects.get(id=pk)
        except Libro.DoesNotExist:
           return HttpResponse(JsonResponse({"libro":"no existe"}),content_type="application/json", status=404)
            
        return HttpResponse(JsonResponse({"libro":libro.get_libro()}),content_type="application/json", status=200)


class BuscarEntreNumeros(APIView):
    def get(self,request,pk1,pk2,format=None):
        lista=[]
        entre_libros=Libro.objects.raw("SELECT * FROM libro_libro WHERE id BETWEEN %s AND %s",[pk1,pk2])
        for entre in entre_libros:
            obj={"id":entre.id,"titulo":entre.titulo,"fecha":entre.fecha}
            lista.append(obj)
        return HttpResponse(JsonResponse({"libro":lista}),content_type="application/json", status=404)

class BuscarEntreNumeros2(APIView):
    def get(self,request,pk1,pk2,format=None):
        lista=[]
        entre_libros=Libro.objects.filter(id__range=(pk1,pk2))
        for entre in entre_libros:
            obj={"id":entre.id,"titulo":entre.titulo,"fecha":entre.fecha}
            lista.append(obj)
        return HttpResponse(JsonResponse({"libro":lista}),content_type="application/json", status=404)


class ExistePorId(APIView):
    def get(self,request,pk,format=None):
        valor=Libro.objects.get(id=pk)
        if valor:
            mensaje="Existe el libro con id:"+str(pk)
            return HttpResponse(JsonResponse({"libro":mensaje}),content_type="application/json", status=200)
        else:
            return HttpResponse(JsonResponse({"libro":"No existe el libro solicitado"}),content_type="application/json", status=404)


class PorNombre(APIView):
    def get(self,request,nombre,format=None):
        lista=[]
        try:
            # libro=Libro.objects.filter(titulo__icontains=nombre)
            # for g in libro:
            #     obj={"id":g.id,"titulo":g.titulo,"fecha":g.fecha}
            #     lista.append(obj)

            libro=Libro.objects.get(titulo__icontains=nombre)
        except Libro.DoesNotExist:
           return HttpResponse(JsonResponse({"libro":"No existe el libro buscado"}),content_type="application/json", status=404)
            
        return HttpResponse(JsonResponse({"libro":libro.get_libro()}),content_type="application/json", status=200)

class buscarEntreFechas(APIView):  
    def get(self,request,f1,f2,format=None):
        libros_lista=[]
        ff1=self.formatear_fecha(f1)
        ff2=self.formatear_fecha(f2)
        libros=Libro.objects.filter(fecha__range=(ff1,ff2))
        for l in libros:
            obj={"id":l.id,"titulo":l.titulo,"fecha":l.fecha}
            libros_lista.append(obj)
        return HttpResponse(JsonResponse({"libros":libros_lista}),content_type="application/json", status=200)

    def formatear_fecha(self,fch1):
        fecha=fch1.split("-")
        dia=""
        mes=""
        ano=""
        fecha_final=""
        if len(fecha)>1:
            dia=fecha[0]
            mes=fecha[1]
            ano=fecha[2]
            fecha_final=ano+'-'+mes+'-'+dia
        return fecha_final 

