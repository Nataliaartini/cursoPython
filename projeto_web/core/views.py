from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

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
    #product = Produto.objects.get(id=pk) #id é o que está no index, quero que o id seja igual o pk que passei para Produto em urlpattern
    product = get_object_or_404(Produto, id=pk) #agora quando a pagina nao existir usuario recebe um 404
    context = {
        'produto': product
    }
    return render(request, 'produto.html', context) #o context é o que vai mostrar o meu produto na pagina produto quando eu clico na sua url

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text.html; charset=utf8', status=500)