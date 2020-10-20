from django.contrib import admin
from django.urls import path

from . import views 
urlpatterns = [
    path('autor_por_libro/<int:pk>',views.AutorId_xlibro.as_view(),name="libros_x_autor"),
    path('listas_categorias_libros/',views.ListarLibroPorCategoria.as_view(),name='lista_categoria_libro'),
    path('libros_prestados/',views.LibrosPrestados.as_view()),
    path('promedio_lectores/',views.PromedioEdadesLectores.as_view()),
    path('listar_libros/',views.BuscarTodosLosLibros.as_view()),
    path('buscar_libro_por_id/<int:pk>',views.BuscarLibroPorId.as_view()),
    path('buscar_libro_entre/<int:pk1>/<int:pk2>',views.BuscarEntreNumeros.as_view()),
    path('buscar_libro_entre2/<int:pk1>/<int:pk2>',views.BuscarEntreNumeros2.as_view()),
    path('buscar_id_existe/<int:pk>',views.ExistePorId.as_view()),
    path('buscar_por_nombre/<str:nombre>',views.PorNombre.as_view()),
    path('buscar_por_fechas/<str:f1>/<str:f2>',views.buscarEntreFechas.as_view()),
    path('tipo_usuario/',views.TipoDeUser.as_view()),
]
