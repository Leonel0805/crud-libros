from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=40)

#creacion modelo libro
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    autor = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    
    


    