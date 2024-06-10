from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from django.views.generic import ListView
from .models import Comentario, Imagen, Sitio
from django.db.models.functions import Trunc
from collections import OrderedDict
from django.db.models import DateField
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImagesForm
from django.db.models import Max
from django.contrib.auth.mixins import LoginRequiredMixin

class GaleriaListView(LoginRequiredMixin, ListView):
    model = Sitio
    template_name = 'galeria_list.html'
    context_object_name = 'galerias'

    def get_queryset(self):
        # Obtiene el usuario actual
        user = self.request.user

        if user.is_superuser:
            # Si el usuario es superusuario, obtiene todos los sitios
            queryset = super().get_queryset().annotate(ultima_fecha_imagen=Max('imagenes__fecha_carga')).prefetch_related('imagenes')
        else:
            # Si no es superusuario, obtiene solo los sitios asociados al perfil del usuario
            queryset = user.userprofile.sitios.annotate(ultima_fecha_imagen=Max('imagenes__fecha_carga')).prefetch_related('imagenes')
        
        for galeria in queryset:
            ultima_imagen = galeria.imagenes.filter(fecha_carga=galeria.ultima_fecha_imagen).first()
            galeria.ultima_imagen = ultima_imagen
        return queryset
    
def galeria_detalle(request, slug):
    sitio = get_object_or_404(Sitio, slug=slug)
    
    # Obtener imágenes y truncar la fecha
    imagenes = Imagen.objects.filter(sitio=sitio).annotate(fecha=Trunc('fecha_carga', 'day', output_field=DateField())).order_by('-fecha')
    
    # Obtener comentarios y truncar la fecha
    comentarios = Comentario.objects.filter(sitio=sitio).annotate(fecha=Trunc('fecha_carga', 'day', output_field=DateField())).order_by('-fecha')
    
    items_por_fecha = OrderedDict()
    
    # Combinar imágenes y comentarios en la misma estructura
    for item in list(imagenes) + list(comentarios):
        items_por_fecha.setdefault(item.fecha, {'imagenes': [], 'comentarios': []})
        if isinstance(item, Imagen):
            items_por_fecha[item.fecha]['imagenes'].append(item)
        elif isinstance(item, Comentario):
            items_por_fecha[item.fecha]['comentarios'].append(item)

    context = {
        'sitio': sitio,
        'items_por_fecha': items_por_fecha,
    }
    return render(request, 'galeria_detail.html', context)


@login_required(login_url='login/')
def fileupload(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            galeria = form.cleaned_data['sitio']
            fecha_carga = form.cleaned_data['fecha_carga']
            comentario_texto = form.cleaned_data.get('comentario') 
            images = request.FILES.getlist('images')  # Asegúrate de que el nombre del campo en el formulario HTML sea 'images'

            imagenes_a_crear = [Imagen(imagen=image, sitio=galeria, fecha_carga=fecha_carga, usuario=request.user) for image in images]

            # Usar bulk_create para mejorar la eficiencia
            Imagen.objects.bulk_create(imagenes_a_crear)

            # Crear y guardar el comentario si existe alguno
            if comentario_texto:  # Verificar si hay algún comentario para guardar
                Comentario.objects.create(sitio=galeria, comentario=comentario_texto, fecha_carga=fecha_carga, usuario=request.user)

            # Añadir un mensaje de éxito
            messages.success(request, "Imágenes cargadas correctamente.")

            return redirect('galeria:galeria_list')
        else:
            messages.error(request, "Se encontraron errores en el formulario, por favor corrígelos.")
            return render(request, "cargar.html", {'form': form})
    else:
        form = ImagesForm()
    
    context = {'form': form}
    return render(request, "cargar.html", context)