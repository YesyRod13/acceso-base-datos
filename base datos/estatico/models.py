from django.db import models

# Create your models here.


class equipo(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.email