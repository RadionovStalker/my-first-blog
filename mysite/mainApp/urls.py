from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # если главная стр. приложения (сайта) mainApp
    path('contact/', views.contact, name='contact'),
]
