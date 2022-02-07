from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    try:
        validate_email(email)
    except:
        messages.error(request, "E-mail inválido.")
        return render(request, "accounts/cadastro.html")

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, "Todos os campos são obrigatórios.")
        return render(request, "accounts/cadastro.html")

    if len(senha) < 6:
        messages.error(request, "Senha deve ter no mínimo 6 caracteres.")
        return render(request, "accounts/cadastro.html")

    if senha != senha2:
        messages.error(request, "Senhas devem ser iguais")
        return render(request, "accounts/cadastro.html")

    if len(usuario) < 6:
        messages.error(request, "Usuário deve ter no mínimo 6 caracteres.")
        return render(request, "accounts/cadastro.html")

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Este nome de usuário já está em uso.")
        return render(request, "accounts/cadastro.html")

    if User.objects.filter(email=email).exists():
        messages.error(request, "Este e-mail já está cadastrado.")
        return render(request, "accounts/cadastro.html")

    messages.success(request, "Registrado com sucesso!")
    return render(request, "accounts/cadastro.html")

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
