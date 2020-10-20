from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('autores/',views.ListAutores.as_view(),name="autores"),
    path('lista_autores/',views.Listar_autores.as_view(),name="lista_autores"),
    path('agregar_autor/',views.AgregarAutor.as_view()),
    path('buscar_edad/<int:edad>',views.BuscarMenoresPorEdad.as_view()),
    path('buscar_autor/<int:pk>',views.Autor_por_id.as_view()),
    path('buscar_autor2',views.Autor_por_id2.as_view()),
    path('buscar_autor3',views.Autor_por_id3.as_view()),
]
