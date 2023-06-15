from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('crear/', views.crear, name='crear'),
    path('crear/libro', views.crear_libro, name='crear_libro'),
    
    
]