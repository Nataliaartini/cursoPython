from django.urls import path

from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato),
    path('produto/<int:pk>', produto, name='produto'), #criando id para importar a url do produto na pagina index
]