from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('trabajos/', views.trabajos_view, name='trabajos'),
]
