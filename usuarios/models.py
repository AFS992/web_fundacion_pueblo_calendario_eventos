from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Usuario(AbstractUser):
    provincia_usuario=models.CharField(max_length=50)
    localidad_usuario=models.CharField(max_length=50)
    telefono_usuario=PhoneNumberField(unique=True, null=False,blank=False)

from calendario.models import Evento

class AsistenciaUsuario(models.Model):
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    


