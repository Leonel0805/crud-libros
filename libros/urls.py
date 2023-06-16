from django.urls import path
from . import views

app_name = 'libroslol'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('crear/', views.crear, name='crear'),
    path('crear/libro/', views.crear_libro, name='crear_libro'),
    path('crear/autor/', views.crear_autor, name='crear_autor'),
    path('crear/editorial/', views.crear_editorial, name='crear_editorial'),
    path('libros/', views.libros, name='libros'),
    path('libros/detalle/<int:id_libro>', views.detalle_libro , name='detalle_libro'),
    path('libros/detalle/<int:id_libro>/eliminar', views.eliminar_libro , name='eliminar_libro'),
    
    
 
]