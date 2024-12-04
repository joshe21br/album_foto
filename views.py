# core/views.py

from django.shortcuts import render, redirect
from .models import Foto
from .forms import FotoForm

def index(request):
    return render(request, 'index.html')  # Caminho relativo à pasta templates

def galeria(request):
    fotos = Foto.objects.all()
    return render(request, 'galeria.html', {'fotos': fotos})  # Caminho relativo à pasta templates

def upload_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = FotoForm()
    return render(request, 'upload_foto.html', {'form': form})  # Caminho relativo à pasta templates
