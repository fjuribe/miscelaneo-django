from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.views import View
from aplications.autor.models import Autor
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

from .forms_persona import ContactoForm
from .models import Persona
from django.views.generic import (
	ListView
)




class ListAllEmpleados(ListView):
	model=Autor
	template_name='persona/list_all.html'

class ListaPorNacionalidad(ListView):
	template_name='persona/list_nacionalidad.html'

	def get_queryset(self):
		valor=self.kwargs['id']
		lista=Autor.objects.get(
			id=valor
		)
		return lista



class Buscar_autor(View):
	template_name="persona/miprueba.html"

	def get(self,request,pk,format=None):
		escritor=Autor.objects.get(id=pk)
		return render(request,self.template_name,{'escrito':escritor.get_autor()})


class AutorADD(View):
	template_name="persona/form_autor.html"

	def get(self,request,format=None):
		return render(request,self.template_name)

	def post(self,request,format=None):
		nombre=request.POST['nombre']
		apellido=request.POST['apellido']
		nacionalidad=request.POST['nacionalidad']
		edad=request.POST['edad']
        
		ad=Autor.objects.create(
			nombre=nombre,
			apellidos=apellido,
			nacionalidad=nacionalidad,
			edad=edad
		)
        
		mensaje=f"su nombre es {nombre} {apellido}"
		return HttpResponse(mensaje)


# class Contacto(View):
# 	submitted=False
# 	template_name='persona/contacto.html'
# 	def post(self,request,format=None):
# 		form=ContactoForm(request.POST)
# 		if form.is_valid():
# 			cd=form.cleanned_data

# 			return HttpResponseRedirect('/contacto?submitted=True')

# 	def get(self,request,format=None):
# 		form=ContactoForm()
# 		if 'submitted' in request.GET:
# 			submitted=True

# 		return render(request,self.template_name,{'form':form,'submitted':submitted})

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
          # assert False
            return HttpResponseRedirect('persona/contacto?submitted=True')
    else:
        form = ContactoForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'persona/contacto.html',{'form': form, 'submitted': submitted})