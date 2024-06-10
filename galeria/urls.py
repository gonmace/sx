from django.urls import path
from galeria.views import GaleriaListView, galeria_detalle, fileupload, update_sitio

app_name = 'galeria'

urlpatterns = [
    path('upload/', fileupload, name='upload'),
    path('edit/<slug:slug>/', update_sitio, name='edit_sitio'),
    path('', GaleriaListView.as_view(), name='galeria_list'),
    path('<slug:slug>/', galeria_detalle, name='galeria_detail'),
]
