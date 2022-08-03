from django.contrib import admin
from .models import Usuario, AsistenciaUsuario




# Register your models here.
@admin.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('id', 'username') #genera una lista en el admin.
    ordering=('username',) #puede ordenar los nombres de ususarios según necesidad.
    search_fields=('username',) #buscador para admin.
    list_display_links=('username',)

@admin.register(AsistenciaUsuario)

class AsistenciaUsuarioAdmin(admin.ModelAdmin):
    list_display=('id', 'id_usuario', 'id_evento', 'id_usuario_asiste')
    list_filter=('id_usuario_asiste','id_evento')
