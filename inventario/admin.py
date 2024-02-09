from django.contrib import admin
from .models import Equipo, EquipoUsuario

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    icon_name='computer'
    search_fields = ('referencia',)
    def get_list_display(self, request):
        return ['id',"referencia","marca", 'tipo']

@admin.register(EquipoUsuario)
class EquipoUsuarioAdmin(admin.ModelAdmin):
    icon_name='confirmation_number'
    search_fields = ('fecha_de_asignacion','usuario__username',)
    def get_list_display(self, request):
        return ['id','equipo','usuario','fecha_de_asignacion','fecha_de_entrega']

