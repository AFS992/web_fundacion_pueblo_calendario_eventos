from django.contrib import admin
from .models import Usuario




# Register your models here.
@admin.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('id', 'username') #genera una lista en el admin.
    ordering=('username',) #puede ordenar los nombres de ususarios según necesidad.
    search_fields=('username',) #buscador para admin.
    list_display_links=('username',)
    list_per_page=20
    

