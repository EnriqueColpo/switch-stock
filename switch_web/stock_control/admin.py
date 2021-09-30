from django.contrib import admin
from .models import Categoria, Marca, Provedor, MarcaProvedor, Cliente, Subcategoria, Producto, Stock, Precio, Venta

# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['marca_id', 'marca_nombre', 'marca_pais']

admin.site.register(Marca, MarcaAdmin)

class ProvedorAdmin(admin.ModelAdmin):
    list_display = [
        'provedor_id',
        'provedor_nombre',
        'provedor_apellido',
        'provedor_email',
        'provedor_telefono'
    ]

admin.site.register(Provedor, ProvedorAdmin)

class MarcaProvedorAdmin(admin.ModelAdmin):
    list_display = [
        'marca_provedor_id',
        'marca',
        'provedor'
    ]

admin.site.register(MarcaProvedor, MarcaProvedorAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'cliente_id',
        'cliente_nombre',
        'cliente_apellido',
        'cliente_email',
        'cliente_telefono'
    ]

admin.site.register(Cliente, ClienteAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'categoria_id',
        'categoria_nombre'
    ]

admin.site.register(Categoria, CategoriaAdmin)

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'subcategoria_id',
        'categoria',
        'descripcion'
    ]

admin.site.register(Subcategoria, SubcategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = [
            'producto_id',
            'marca',
            'categoria',
            'producto_nombre',
            'descripcion',
            'imagen',
            'image_tag'
    ]

admin.site.register(Producto, ProductoAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display = [
        'stock_id',
        'producto',
        'subcategoria',
        'color',
        'talle',
        'cantidad_disponible',
    ]

admin.site.register(Stock, StockAdmin)

class PrecioAdmin(admin.ModelAdmin):
    list_display = [
        'precio_id',
        'producto',
        'subcategoria',
        'precio_costo',
        'precio_publico',
        'fecha_actualizacion'
    ]

admin.site.register(Precio, PrecioAdmin)

class VentaAdmin(admin.ModelAdmin):
    list_display = [
        'venta_id',
        'producto',
        'fecha',
        'medio',
        'monto'

    ]

admin.site.register(Venta, VentaAdmin)
