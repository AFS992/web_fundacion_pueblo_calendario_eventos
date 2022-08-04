from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Usuario(AbstractUser):
    provincia_usuario=models.CharField(max_length=50)
    localidad_usuario=models.CharField(max_length=50)
    #confirmacion_asisetencia=models.BooleanField(default=False)
    
    




    


