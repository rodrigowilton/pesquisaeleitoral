# pesquisa/views.py

from django.shortcuts import render, redirect
from .forms import PesquisaForm

def pesquisa_create(request):
    if request.method == 'POST':
        form = PesquisaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pesquisa_success')
    else:
        form = PesquisaForm()
    return render(request, 'pesquisa/pesquisa_form.html', {'form': form})

def pesquisa_success(request):
    return render(request, 'pesquisa/pesquisa_success.html')
