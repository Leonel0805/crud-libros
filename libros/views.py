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
                return redirect('libroslol:crear_libro')
            
            elif opcion == 'autor':
                return redirect('libroslol:crear_autor')
                    
            elif opcion == 'editorial':
                pass 
            
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
    
    form = AutorCreateForm()
    
    if request.method == 'GET':
        return render(request, 'crear_autor.html',{
            'form':form
        })
        
    elif request.method == 'POST':
        form = AutorCreateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('libroslol:libros')
        
        else:
            return render(request, 'crear_autor.html',{
                'form': form,
                'error': 'Error al crear autor'
            })
        

def crear_libro(request):
    
    form = LibroCreateForm()
    
    if request.method == 'GET':
        return render(request, 'crear_libro.html',{
            'form':form
        })
        
    elif request.method == 'POST':
        form = LibroCreateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('libroslol:libros')
        
        else:
            return render(request, 'crear_libro',{
                'form': form,
                'error': 'Error al crear libro'
            })
            
            

def libros(request):
    pass