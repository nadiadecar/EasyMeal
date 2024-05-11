from django.shortcuts import render

# Create your views here.
def inicio(request): 
    return render(request, 'recetas/index.html', {})

def listado_recetas(request): 
    return render(request, 'recetas/listado_recetas.html', {})