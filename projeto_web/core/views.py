from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all
    context = {
        "curso": "qualquer texto aqui",
        "produtos": produtos
    }
    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")

def produto(request, pk): #pk que é passado no url de acesso a pagina produto urlpattern
    product = Produto.objects.get(pk=pk)
    context = {
        'produto': product
    }
    return render(request, 'produto.html', context) #o context é o que vai mostrar o meu produto na pagina produto quando eu clico na sua url
