from django.shortcuts import render, redirect, get_object_or_404
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
                return redirect('libroslol:crear_editorial') 
            
            return render(request, 'crear.html',{
            'form': form
        })  
        else:
            return render(request, 'crear.html',{
                'form': form,
                'error': 'Error'
            })
            

def crear_editorial(request):

    form = EditorialCreateForm()
    
    if request.method == 'GET':
        return render(request, 'crear_editorial.html',{
            'form': form
        })
        
    elif request.method == 'POST':
        form = EditorialCreateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('libroslol:libros')
    
        else:
            return render(request, 'crear_editorial'),{
                'form':form,
                'error': 'Error al crear editorial'
            }
            
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
        #hace falta request.FILES para las imagenes guardarlas
        #recibidas por el formulario
        form = LibroCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('libroslol:libros')
        
        else:
            return render(request, 'crear_libro',{
                'form': form,
                'error': 'Error al crear libro'
            })
            
            

def libros(request):
    
    libros = Libro.objects.all()
    
    return render(request, 'libros.html',{
        'libros':libros
    })
    
#actualizar datos de libro
def detalle_libro(request, id_libro):
    
    libro = get_object_or_404(Libro, pk=id_libro)
    form = LibroCreateForm(instance=libro)
    
    if request.method == 'GET':
        return render(request, 'detalle_libro.html',{
            'libro':libro,
            'form':form
        })
        
    elif request.method == 'POST':
        form = LibroCreateForm(request.POST, request.FILES, instance=libro)
        
        if form.is_valid():
            form.save()
            return redirect('libroslol:libros')
        
        else:
            return render(request, 'detalle_libro.html',{
            'libro':libro,
            'form':form,
            'error':'Error al actualizar'
        })
    
    
def eliminar_libro(request, id_libro):
    
    libro = get_object_or_404(Libro, pk = id_libro)
    
    libro.delete()
    return redirect('libroslol:libros')
    