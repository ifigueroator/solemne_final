from django.contrib import admin

from mantenedor.models import registro_cliente,nuevos_plan

class nuevoCliente(admin.ModelAdmin):
    list_display=("nombre","apellidoP","apellidoM","email","telefono")
    search_fields=("nombre","apellidoP","apellidoM","email","telefono")


class registro(admin.ModelAdmin):
    list_display=("nombre_plan","precio_plan","fecha_inicio","fecha_termino")
    

admin.site.register(registro_cliente,nuevoCliente)
admin.site.register(nuevos_plan,registro) 
# Register your models here.
