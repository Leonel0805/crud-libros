from django.forms import ModelForm
from .models import Autor, Libro, Editorial, Crear

class AutorCreateForm(ModelForm):
    class Meta: 
        model = Autor
        fields = ['nombre', 'email']
        
class LibroCreateForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'descripcion','autor', 'editorial']
        
class EditorialCreateForm(ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre']
        
class CrearCreateForm(ModelForm):
    class Meta:
        model = Crear
        fields = ['opcion']