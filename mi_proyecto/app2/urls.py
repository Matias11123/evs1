from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio_app2, name='inicio_app2'),
    path('contacto/', views.contacto_app2, name='contacto_app2'),
]