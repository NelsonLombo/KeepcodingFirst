# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC
# Create your views here.

def home(request):
    """
    Esta funcion devuelve el home de mi pagina
    """

    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list':photos[:5]
    }
    return render(request, 'photos/home.html',context)


def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttPRequest
    :param id: id de la foto
    :return: HttPResponse
    """
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        #cargar plantilla de detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto') # 404 not found
