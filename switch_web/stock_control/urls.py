from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from stock_control.views import HomeView
from stock_control.views import AgregarMarcaView
from stock_control.views import AgregarProvedorView
from stock_control.views import AgregarMarcaProvedorView
from stock_control.views import AgregarClienteView
from stock_control.views import AgregarCategoriaView
from stock_control.views import AgregarSubcategoriaView
from stock_control.views import AgregarProductoView

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('agregar-marca', AgregarMarcaView.as_view()),
    path('agregar-provedor', AgregarProvedorView.as_view()),
    path('agregar-marca-provedor', AgregarMarcaProvedorView.as_view()),
    path('agregar-cliente', AgregarClienteView.as_view()),
    path('agregar-categoria', AgregarCategoriaView.as_view()),
    path('agregar-subcategoria', AgregarSubcategoriaView.as_view()),
    path('agregar-producto', AgregarProductoView.as_view())

]

# urlpatterns = format_suffix_patterns(urlpatterns)