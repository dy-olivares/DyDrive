from django.db import models

# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(upload_to="media/", blank=True, null=True )
    
    
class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    text = models.TextField(verbose_name="Texto")
    color = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ["-created"]

    def __str__(self):
        return self.title

    
class Perfil(models.Model):
    name = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to="media/", blank=True, null=True )
