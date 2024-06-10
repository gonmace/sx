from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.documentation import include_docs_urls

# router = routers.DefaultRouter()
# router.register(r'alcance', views.AlcanceViewSet, 'alcance')

urlpatterns = [
    path('', views.home),
    path('login/', views.CustomLoginView.as_view(), name='login')
    
    # path('api/v1/', include(router.urls)),
    # path('docs/', include_docs_urls(title='Alcance API')),
]