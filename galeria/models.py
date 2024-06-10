from django.db import models
from django.utils.text import slugify
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class Sitio(models.Model):
    sitio = models.CharField("Codigo Sitio", max_length=10, unique=True) 
    nombre = models.CharField(max_length=100, blank=True)
    lat = models.FloatField("Latitud", max_length=11, blank=True, null=True)
    lon = models.FloatField("Longitud", max_length=11, blank=True, null=True)
    slug = models.SlugField(max_length=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sitio)[:10]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.sitio} {self.nombre}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sitios = models.ManyToManyField(Sitio)

    def __str__(self):
        return self.user.username



class Imagen(models.Model):
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes/')
    fecha_carga = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='imagenes_subidas')

    def __str__(self):
        return f"{self.sitio} - {self.fecha_carga}"


class Comentario(models.Model):
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='comentario')
    comentario = models.TextField(blank=True, null=True)
    fecha_carga = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios_subidas')

    def __str__(self):
        return f"{self.sitio} - {self.comentario}"
