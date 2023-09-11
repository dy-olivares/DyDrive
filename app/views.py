from django.shortcuts import render
from .models import *
def inicio(request):
    
    import random
    photos = Photo.objects.all()
    photosCount = photos.count()
    
    numero = random.randint(1, photosCount)
    
    photo_randon = Photo.objects.get(id=numero)
    
    perfil = Perfil.objects.get(id=1)
        
    
    context = {
        'perfil':perfil,
        'photos':photos,
        'photo_randon':photo_randon,
    }
    return render(request, 'app/inicio.html', context)