from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_evento_cultural, name='criar_evento_cultural'),
]


