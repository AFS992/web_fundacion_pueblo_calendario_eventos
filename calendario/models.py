from django.db import models
#from usuarios.models import Usuario
#import usuarios.models
from usuarios.models import Usuario


#foo=usuarios.models.AsistenciaUsuario()
# Create your models here.

#Creamos la tabla de caterías a parte para poder filtrar después.
class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre_categoria}'

# Creamos la tabla de eventos con sus respectivos campos.
class Evento(models.Model):
    autor_evento=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo_evento=models.CharField(max_length=50)
    fecha_evento=models.DateField()
    hora_evento=models.CharField(max_length=5)
    modalidad_evento=models.CharField(max_length=50)
    descripcion_evento=models.TextField()
    id_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #asistentes_esperados=models.ForeignKey(AsistenciaUsuario, on_delete=models.PROTECT) --> falta corregir errores

    def __str__(self):
        return f'{self.titulo_evento} {self.fecha_evento} {self.hora_evento} {self.modalidad_evento} {self.descripcion_evento}'








