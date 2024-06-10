from django.contrib import admin
from galeria.models import Comentario, Imagen, Sitio, UserProfile


# class SitioAdmin(admin.ModelAdmin):
#     list_display = ('sitio', 'nombre', 'lat', 'lon', 'slug')
# admin.site.register(Sitio, SitioAdmin)
admin.site.register(UserProfile)

admin.site.register(Sitio)

admin.site.register(Imagen)

admin.site.register(Comentario)
