from django.db import models

# Create your models here.
class Equipos(models.Model):
    nombre = models.CharField(max_length=50, blank=False, default='')
    fundacion = models.CharField(max_length=25, blank=False, default='')
    apodo = models.CharField(max_length=50, blank=False, default='')
    ciudad = models.CharField(max_length=50, blank=False, default='')
    nombre_estadio = models.CharField(max_length=50, blank=False, default='')

    # imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,default='')


    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering= ('id',)


