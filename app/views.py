# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index_page(request):
    return render(request, 'index.html')

def home(request):
    """
    Vista principal que muestra la galería de personajes de Los Simpsons.
    
    Esta función debe obtener el listado de imágenes desde la capa de servicios
    y también el listado de favoritos del usuario, para luego enviarlo al template 'home.html'.
    Recordar que los listados deben pasarse en el contexto con las claves 'images' y 'favourite_list'.
    """
    "cambio de prueba"
    "cambios de prueba 2"
    images= services.getAllImages()
    favourite_list = []
    if request.user.is_authenticated:
        
        favourite_list = services.getAllFavourites(request.user)
    
    return render(request, 'home.html', {'images': images,'favourite_list': favourite_list})

def search(request):
    """
    Busca personajes por nombre.
    
    Se debe implementar la búsqueda de personajes según el nombre ingresado.
    Se debe obtener el parámetro 'query' desde el POST, filtrar las imágenes según el nombre
    y renderizar 'home.html' con los resultados. Si no se ingresa nada, redirigir a 'home'.
    """
    name = request.POST.get('query','').lower()
    if name:
            images = [img for img in services.getAllImages()
            if name in img.name.lower()]
            favourite_list = services.getAllFavouritesByUser(request.user) \
                if request.user.is_authenticated else []
            return render(request, 'home.html', {
            'images': images,
            'favourite_list': favourite_list
        })
    else:
            return redirect('home')


def filter_by_status(request):
    """
    Filtra personajes por su estado (Alive/Deceased).
    
    Se debe implementar el filtrado de personajes según su estado.
    Se debe obtener el parámetro 'status' desde el POST, filtrar las imágenes según ese estado
    y renderizar 'home.html' con los resultados. Si no hay estado, redirigir a 'home'.
    """
    type_filter= request.POST.get('status', '').lower()
    if type_filter:
        images = [img for img in services.getAllImages() if type_filter in img.status.lower()]
        return render (request, 'home.html',{'images': images})
    else:
        return redirect('home')

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    """
    pass

@login_required
def saveFavourite(request):
    """
    Guarda un personaje como favorito.
    
    """

@login_required
def deleteFavourite(request):
    """
    Elimina un favorito del usuario.
    """
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')