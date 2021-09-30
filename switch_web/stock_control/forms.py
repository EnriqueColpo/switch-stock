# django

from django import forms

from stock_control.models import Marca
from stock_control.models import Provedor
from stock_control.models import MarcaProvedor
from stock_control.models import Cliente
from stock_control.models import Categoria
from stock_control.models import Subcategoria
from stock_control.models import Producto
from stock_control.models import Stock
from stock_control.models import Precio
from stock_control.models import Venta


class BrandForm(forms.ModelForm):
    """Post models form"""
    
    class Meta:
        """Form settings."""

        model = Marca
        fields = ('marca_nombre', 'marca_pais')


class ProviderForm(forms.ModelForm):
    """Provider model form"""

    class Meta:
        """Form settings."""
        

        model = Provedor
        fields = (
            'provedor_nombre',
            'provedor_apellido',
            'provedor_email',
            'provedor_telefono'
        )


class MarcaProvedorForm(forms.ModelForm):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), initial=0)
    provedor = forms.ModelChoiceField(queryset=Provedor.objects.all(), initial=0)

    class Meta:
        model = MarcaProvedor
        fields = ('marca', 'provedor')


class ClienteForm(forms.ModelForm):
    """ Cliente model form """

    class Meta:

        model = Cliente
        fields = (
            'cliente_nombre',
            'cliente_apellido',
            'cliente_email',
            'cliente_telefono'
        )


class CategoriaForm(forms.ModelForm):
    """Categoria model form"""

    class Meta:

        model = Categoria
        fields = ('categoria_nombre',)


class SubcategoriaForm(forms.ModelForm):
    """Categoria model form"""
    class Meta:

        model = Subcategoria
        fields = ('categoria', 'descripcion')


class ProductoForm(forms.ModelForm):
    """Categoria model form"""

    class Meta:

        model = Producto
        fields = (
            'marca',
            'categoria', 
            'subcategoria',
            'producto_nombre',
            'descripcion',
            'imagen'
        )


class StockForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), initial=0)
    subcategoria = forms.ModelChoiceField(queryset=Subcategoria.objects.all(), initial=0)
    
    class Meta:

        model = Stock
        fields = (
            'producto',
            'subcategoria',
            'color',
            'talle',
            'cantidad_disponible'
        )


class PrecioForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), initial=0)
    subcategoria = forms.ModelChoiceField(queryset=Subcategoria.objects.all(), initial=0)
    
    class Meta:
        model = Precio
        fields = (
            'producto',
            'subcategoria',
            'precio_costo',
            'precio_publico',
        )


class VentaForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), initial=0)
    
    class Meta:
        model = Venta
        fields = (
            'producto',
            'medio',
            'monto'
        )

