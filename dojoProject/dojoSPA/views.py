from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def contacto_view(request):
    return render(request, 'contacto.html')

def trabajos_view(request):
    return render(request, 'trabajos.html')
