from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre

#creacion modelo libro
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    portada = models.ImageField(upload_to='libroslol/imagenes', blank=True)
    autor = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    
class Crear(models.Model):
    
    OPCIONES= [
        ('libro', 'LIBRO'),
        ('autor', 'AUTOR'),
        ('editorial', 'EDITORIAL')
    ]
    
    opcion = models.CharField(max_length=50, choices=OPCIONES)
    


    