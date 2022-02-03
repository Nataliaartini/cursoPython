from django.shortcuts import render

def index(request):
    return render(request, 'example/index.html')

def sobre(request):
    return render(request, 'example/sobre.html')
