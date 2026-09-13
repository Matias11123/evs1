from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_app1, name='inicio_app1'),
    path('detalle/', views.detalle_app1, name='detalle_app1'),
]