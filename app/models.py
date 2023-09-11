from django.db import models

# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(upload_to="media/", blank=True, null=True )
    
    
    
class Perfil(models.Model):
    name = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to="media/", blank=True, null=True )
