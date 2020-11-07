from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#modelo local
from .models import Autor
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


##########################3

# Create your views here.
class ListAutores(APIView):
    def get(self,format=None):
        numero=Autor.objects.all()
        existe=None
        if len(numero)>0:
            existe=len(numero)
        else:
            existe=False   
        return HttpResponse(JsonResponse({"Autor":existe}),content_type="application/json", status=200)


class Listar_autores(APIView):
    def get(self,request,format=None):

        lista=[]
        autores=Autor.objects.all()

        ################# PAGINACION ########################
        paginator = Paginator(autores,10)

        pagina = request.GET.get('page', 1)

        pagina = int(pagina)

        try:
            docs = paginator.page(pagina)
        except EmptyPage:
			# If page is not an integer, deliver first page.
            docs = paginator.page(1)

        page = docs 

        #######################################
        for autor in docs:
            obj={"id":autor.id,"titulo":autor.nombre,"fecha":autor.apellidos,"portada":autor.nacionalidad,"edad":autor.edad}
            lista.append(obj)

        return HttpResponse(JsonResponse({"autores":lista, 'pager':{'current_page': page.number, 'last_page': page.paginator.num_pages}, "total_records":len(lista)}),content_type="application/json", status=200)


#http://localhost:8000/buscar_autor/2
class Autor_por_id(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    def get(self,request,pk,format=None):
        try:
            autor=Autor.objects.get(id=pk)
        except Autor.DoesNotExist:
            return HttpResponse(JsonResponse({"autor":"No existe"}),content_type="application/json", status=404)
        return HttpResponse(JsonResponse({"autor":autor.get_autor()}),content_type="application/json", status=200)


#http://localhost:8000/buscar_autor2?id=2
class Autor_por_id2(APIView):
    def get(self,request,format=None):
        pk=request.GET.get('id','')
        try:
            autor=Autor.objects.get(id=pk)
        except Autor.DoesNotExist:
            return HttpResponse(JsonResponse({"autor":"No existe"}),content_type="application/json", status=404)
        return HttpResponse(JsonResponse({"autor":autor.get_autor()}),content_type="application/json", status=200)


#http://localhost:8000/buscar_autor3
class Autor_por_id3(APIView):
    def post(self,request,format=None):
        pk=request.data['id']
        try:
            autor=Autor.objects.get(id=pk)
        except Autor.DoesNotExist:
            return HttpResponse(JsonResponse({"autor":"No existe"}),content_type="application/json", status=404)
        return HttpResponse(JsonResponse({"autor":autor.get_autor()}),content_type="application/json", status=200)



###############################################################################################################

class BuscarMenoresPorEdad(APIView):
    def get(self,request,edad,format=None):
        lista=[]
        autores=Autor.objects.filter(edad__gt=edad)
        for au in autores:
            lista.append(au.get_autor2())
        return HttpResponse(JsonResponse({"autor":lista,"total":autores.count()}),content_type="application/json", status=200)

class AgregarAutor(APIView):
    def post(self,request,format=None):
        nombre=request.data["nombre"]
        apellido=request.data["apellido"]
        nacionalidad=request.data["nacionalidad"]
        edad=request.data["edad"]
        agregar=Autor.objects.create(
            nombre=nombre,
            apellidos=apellido,
            nacionalidad=nacionalidad,
            edad=edad
        )
        return HttpResponse(JsonResponse({"success":"agregado exitosamente","autor":agregar.get_autor()}),content_type="application/json", status=200)

##########################################################################################3333
# class GestionCalendario(APIView):
#     def post(self,request,format=None):
#         start=None
#         title=None
#         color=[]
#         actions=None
#         draggable=None

#         if 'start' in request.data:
#             start=request.data['start']

#         if 'title'  in request.data:
#             title=request.data['title']

#         if 'color' in request.data:
#             color=request.data['color']
#             for col in color:


        
        
#         color=request.data['color']
#         actions=request.data['actions']
#         draggable=request.data['draggable']





