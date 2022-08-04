from django.db import models
from usuarios.models import Usuario
from calendario.models import Evento

# Create your models here.
class AsistenciaUsuario(models.Model):
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    id_usuario_asiste=models.BooleanField(default=False)