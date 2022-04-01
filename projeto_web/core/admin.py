from django.contrib import admin
from .models import Produto, Cliente

#aqui estou criando o modo como eu quero ver meu produto no admin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

#para puxar a classe que eu defini o que quero ver no admin eu passo ela como parametro no register do produto
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)
