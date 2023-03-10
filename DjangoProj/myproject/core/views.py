from django.shortcuts import render, redirect
from .models import Jogo
from .forms import JogoForm


def index(request):
    data = {}
    data['jogos'] = Jogo.objects.all()
    return render(request, 'core/index.html', data)


def formJogo(request):
    data = {}
    j = JogoForm(request.POST or None)
    if j.is_valid():
        j.save()
        return redirect('index')
    data['form'] = j
    return render(request, 'core/formJogo.html', data)


def update(request, pk):
    data = {}
    k = Jogo.objects.get(pk=pk)
    j = JogoForm(request.POST or None, instance=k)
    if j.is_valid():
        j.save()
        return redirect('index')
    data['form'] = j
    return render(request, 'core/formJogo.html', data)


def delete(request, pk):
    j = Jogo.objects.get(pk=pk)
    j.delete()
    return redirect('index')
