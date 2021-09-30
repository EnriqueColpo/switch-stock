from django.db import models
from django.utils.safestring import mark_safe

class Marca(models.Model):
    marca_id = models.BigAutoField(primary_key=True)
    marca_nombre = models.CharField("Nombre de la marca", max_length=30)
    marca_pais = models.CharField("Pais de la marca", max_length=30)

    def __str__(self):
        return self.marca_nombre

    class Meta:
        ordering = ['marca_id']


class Provedor(models.Model):
    provedor_id = models.BigAutoField(primary_key=True)
    provedor_nombre = models.CharField("Nombre", max_length=30)
    provedor_apellido = models.CharField("Apellido", max_length=30)
    provedor_email = models.CharField("Email", max_length=30)
    provedor_telefono = models.CharField("Telefono", max_length=30)
    
    class Meta:
        ordering = ['provedor_id']
        verbose_name_plural = 'Provedores'

    def __str__(self):
        return self.provedor_nombre  # or you can use any string value instead of campaign_name


class MarcaProvedor(models.Model):
    marca_provedor_id = models.BigAutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    provedor = models.ForeignKey(Provedor, on_delete=models.CASCADE)

    class Meta:
       ordering = ['marca_provedor_id']
       verbose_name_plural = 'Marcas Provedores'

    def __str__(self):
        return f"{self.marca}, {self.provedor}"


class Cliente(models.Model):
    cliente_id = models.BigAutoField(primary_key=True)
    cliente_nombre = models.CharField("Nombre", max_length=30)
    cliente_apellido = models.CharField("Apellido", max_length=30)
    cliente_email = models.CharField("Email", max_length=30)
    cliente_telefono = models.CharField("Telefono", max_length=30)

    class Meta:
       ordering = ['cliente_id']


class Categoria(models.Model):
    categoria_id = models.BigAutoField(primary_key=True)
    categoria_nombre = models.CharField("Categoria", max_length=30)

    class Meta:
        ordering = ['categoria_id']

    def __str__(self):
        return self.categoria_nombre


class Subcategoria(models.Model):
    subcategoria_id = models.BigAutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.CharField("Subcategoria", max_length=30)

    def __str__(self):
        return self.descripcion

    class Meta:
       ordering = ['subcategoria_id']


class Producto(models.Model):
    producto_id = models.BigAutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    producto_nombre = models.CharField("Nombre", max_length=15)
    descripcion = models.CharField("Descripcion", max_length=30)
    imagen = models.ImageField(upload_to='images/', null=True)

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.imagen))
    
    image_tag.allow_tags = True  

    class Meta:
        ordering = ['producto_id']

    def __str__(self):
        return self.producto_nombre


class Stock(models.Model):
    stock_id = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    color = models.CharField("Color", max_length=30)
    talle = models.CharField("Talle", max_length=30)
    cantidad_disponible = models.IntegerField()

    class Meta:
        ordering = ['stock_id']


class Precio(models.Model):
    precio_id = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    precio_costo = models.IntegerField()
    precio_publico = models.IntegerField()
    fecha_actualizacion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['precio_id']


class Venta(models.Model):
    venta_id = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    medio = models.CharField("person's first name", max_length=30)
    monto = models.IntegerField()

    class Meta:
        ordering = ['venta_id']
