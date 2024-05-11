from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('/recetas/', views.listado_recetas, name='recetas')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)