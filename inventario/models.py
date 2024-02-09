from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    referencia = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    procesador = models.CharField(max_length=150)
    memoria = models.CharField(max_length=150)
    disco = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)    

    def __str__(self):
        return f"{self.referencia}"

class EquipoUsuario(models.Model):
    fecha_de_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_de_entrega = models.DateTimeField(null=True, blank=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)   

    def __str__(self):
        return f"{self.equipo} {self.usuario}"
