from django.shortcuts import render, redirect
from .models import Autor, Libro, Editorial, Crear
from .forms import AutorCreateForm, LibroCreateForm, EditorialCreateForm, CrearCreateForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def crear(request):
    
    form = CrearCreateForm()
    
    if request.method == 'GET':
        return render(request, 'crear.html',{
            'form': form
        })
    
    elif request.method == 'POST':
        form = CrearCreateForm(request.POST)
        
        if form.is_valid():
            opcion = form.cleaned_data['opcion']
            
            if opcion == 'libro':
                return redirect('libros:crear_libro')
            
            return render(request, 'crear.html',{
            'form': form
        })  
        else:
            return render(request, 'crear.html',{
                'form': form,
                'error': 'Error'
            })
            

def crear_editorial(request):
    pass
def crear_autor(request):
    pass

def crear_libro(request):
    
    return render(request, 'crear_libro.html')

def libros(request):
    pass