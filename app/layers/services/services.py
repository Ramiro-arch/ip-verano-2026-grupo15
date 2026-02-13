# capa de servicio/lógica de negocio

import random
from ..transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages():
    """
    Obtiene todas las imágenes de personajes desde la API y las convierte en objetos Card.

    Esta función debe obtener los datos desde transport, transformarlos en Cards usando 
    translator y retornar una lista de objetos Card.
    """
    
    images = transport.getAllImages()
    cards = []
    for image in images:
        card = translator.fromRequestIntoCard(image)
        if card.phrases and len(card.phrases)>0:
            fraseCorta= card.phrases[0]
            for frase in card.phrases:
                if len(frase)< len(fraseCorta):
                    fraseCorta=frase
            card.phrases=fraseCorta
        cards.append(card)
    return cards

def filterByCharacter(name):
    """
    Filtra las cards de personajes según el nombre proporcionado.
    
    Se debe filtrar los personajes cuyo nombre contenga el parámetro recibido. Retorna una lista de Cards filtradas.
    """
    cards= getAllImages()
    cardsFiltradasSegunNombre=[]
    for card in cards:
        if name.lower() in card.name.lower():
            cardsFiltradasSegunNombre.append(card)
    return cardsFiltradasSegunNombre

def filterByStatus(status_name):
    """
    Filtra las cards de personajes según su estado (Alive/Deceased).
    
    Se deben filtrar los personajes que tengan el estado igual al parámetro 'status_name'. Retorna una lista de Cards filtradas.
    """
    cards=getAllImages()
    cardsFiltradasPorEstado=[]
    for card in cards:
        if card.status and card.status.lower() == status_name.lower():
            cardsFiltradasPorEstado.append(card)
    return cardsFiltradasPorEstado
# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    """
    Guarda un favorito en la base de datos.
    
    Se deben convertir los datos del request en una Card usando el translator,
    asignarle el usuario actual, y guardarla en el repositorio.
    """
    

def getAllFavourites(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    
    Si el usuario está autenticado, se deben obtener sus favoritos desde el repositorio,
    transformarlos en Cards usando translator y retornar la lista. Si no está autenticado, se retorna una lista vacía.
    """

def deleteFavourite(request):
    """
    Elimina un favorito de la base de datos.
    
    Se debe obtener el ID del favorito desde el POST y eliminarlo desde el repositorio"""
        
        
        