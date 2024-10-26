from django.contrib import admin
from . import models    
from django.utils.html import format_html

admin.site.site_header = 'Administración Clientes'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Cliente'




class ClientesAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre', 'apellido', 'direccion', 'telefono', 'fecha_alta')
    list_display = ('nombre', 'apellido', 'direccion', 'listar_promociones')

    def listar_promociones(self, obj):
        promociones = obj.promociones.all()  # 'promociones' es el related_name que usamos en PromoPorCliente
        if promociones:
            return format_html(", ".join([str(promo.promo) for promo in promociones]))
        return "No tiene promociones"
    
    listar_promociones.short_description = 'Promociones'

admin.site.register(models.Cliente, ClientesAdmin)

# class ClientesAdmin(admin.ModelAdmin): # ORIGINAL
#     readonly_fields = ('nombre','apellido', 'direccion', 'telefono', 'fecha_alta','fecha_cobro')
#     list_display = ('nombre','apellido', 'direccion','fecha_cobro')

# admin.site.register(models.Cliente, ClientesAdmin)

# class PromoAdmin(admin.ModelAdmin):
#     readonly_fields = ('cant_bidones','nombre_promo')
#     list_display = ('nombre_promo','cant_bidones','valor_promo')

# admin.site.register(models.Promo, PromoAdmin)

class PromoPorClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('cliente','promo','inicio_promo','fin_promo', 
    'fecha_pago_promo', 'bidones_disponibles', 'entrega_bidones','retorno_bidones',
    'bidones_acumulados','codigo_dispenser','nota')
    list_display = ('id','cliente','promo','fecha_pago_promo', 'inicio_promo','estado')

admin.site.register(models.PromoPorCliente, PromoPorClienteAdmin)

# class VisitaAdmin(admin.ModelAdmin):
#     readonly_fields = ('cliente','fecha_visita','nota')
#     list_display = ('fecha_visita', 'cliente')

# admin.site.register(models.Visita, VisitaAdmin)

# class VentaAdmin(admin.ModelAdmin):
#     readonly_fields = ('cliente', 'fecha_venta', 'total_venta', 'nota')
#     list_display = ('cliente', 'fecha_venta')

# admin.site.register(models.Venta, VentaAdmin)

# class ProductoAdmin(admin.ModelAdmin):
#     readonly_fields = ('nombre_producto', 'precio_producto', 'stock', 'estado')
#     list_display = ('nombre_producto', 'precio_producto', 'stock', 'estado')

# admin.site.register(models.Producto, ProductoAdmin)

# class VentaProductoAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'fecha', 'venta', 'producto', 'descuento', 'precio_unidad_venta', 'cantidad','precio_total_venta')
#     list_display = ('id', 'fecha','venta', 'producto', 'cantidad','precio_total_venta')

# admin.site.register(models.VentaProducto, VentaProductoAdmin)


# class PagoAdmin(admin.ModelAdmin):
#     readonly_fields = ('fecha_pago', 'venta', 'promo','cliente', 'monto','metodo_pago', 'descripcion')
#     list_display = ('fecha_pago', 'cliente', 'monto','metodo_pago', 'descripcion')

# admin.site.register(models.Pagos, PagoAdmin)