from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('escritores/',views.ListAllEmpleados.as_view(),name="escritores"),
    path('escritor_nacionalidad/<int:id>/',views.ListaPorNacionalidad.as_view()),
    path('buscar/<int:pk>',views.Buscar_autor.as_view()),
    path('formulario/',views.AutorADD.as_view()),
    path('contacto/',views.contact),
]
