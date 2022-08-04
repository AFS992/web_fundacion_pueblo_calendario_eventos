from django.contrib import admin
from .models import AsistenciaUsuario


# Register your models here.
@admin.register(AsistenciaUsuario)

class AsistenciaUsuarioAdmin(admin.ModelAdmin):
    list_display=('id_usuario','id_evento','id_usuario_asiste')
    exclude=('id_usuario_asiste',)

    def has_add_permissions(self,request):
        return False

    def has_delete_permissions(self,request,obj=None):
        return False