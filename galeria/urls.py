from django.urls import path
from galeria.views import GaleriaListView, galeria_detalle, fileupload

app_name = 'galeria'

urlpatterns = [
    path('upload/', fileupload, name='upload'),
    path('', GaleriaListView.as_view(), name='galeria_list'),
    path('<slug:slug>/', galeria_detalle, name='galeria_detail'),
]
