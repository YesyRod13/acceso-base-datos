from django.urls import path
from estatico import views

urlpatterns = [
    path('', views.index, name='index')
]