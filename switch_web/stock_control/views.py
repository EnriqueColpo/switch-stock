from django.shortcuts import render
from django.views.generic import ListView, CreateView

from stock_control.forms import BrandForm
from stock_control.forms import MarcaProvedorForm
from stock_control.forms import ProviderForm
from stock_control.forms import ClienteForm
from stock_control.forms import CategoriaForm
from stock_control.forms import SubcategoriaForm
from stock_control.forms import ProductoForm
from stock_control.forms import StockForm
from stock_control.forms import PrecioForm
from stock_control.forms import VentaForm


# Create your views here.
from .models import Producto


class HomeView(ListView):
    template_name = "home.html"
    model = Producto
    paginate_by = 5
    context_object_name = 'productos'

class AgregarMarcaView(CreateView):
    """Crea un nuevo registro de marca"""

    template_name = "agregar-marca.html"
    form_class = BrandForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AgregarProvedorView(CreateView):
    """Crea un nuevo registro de provedor"""

    template_name = "agregar-provedor.html"
    form_class = ProviderForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class AgregarMarcaProvedorView(CreateView):
    """Crea un nuevo registro de marca-provedor"""
    template_name = "marca-provedor.html"
    form_class = MarcaProvedorForm
    success_url = '/stock_control/home'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AgregarClienteView(CreateView):
    """Agrega un nuevo cliente a la base de datos"""
    
    template_name = 'agregar-cliente.html'
    form_class = ClienteForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AgregarCategoriaView(CreateView):
    """ """

    template_name = 'agregar-categoria.html'
    form_class = CategoriaForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AgregarSubcategoriaView(CreateView):
    """ """

    template_name = 'agregar-subcategoria.html'
    form_class = SubcategoriaForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AgregarProductoView(CreateView):
    """ """

    template_name = 'agregar-producto.html'
    form_class = ProductoForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CrearStock(CreateView):
    """ """

    template_name = ''
    form_class = StockForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CrearPrecio(CreateView):
    """ """

    template_name = ''
    form_class = PrecioForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CrearVenta(CreateView):
    """ """

    template_name = ''
    form_class = VentaForm
    success_url = '/stock_control/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context