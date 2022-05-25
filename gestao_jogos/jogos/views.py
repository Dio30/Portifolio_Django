from django.shortcuts import render, redirect, get_object_or_404
from .models import Games
from .forms import GamesForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def games_list(request):
    pesquisar = request.GET.get('pesquisa', None)
    if pesquisar:
        games = Games.objects.filter(nome_do_jogo__icontains=pesquisar)
    else:
        games = Games.objects.all()
    return render(request, 'jogos.html', {'games': games})

@login_required
def games_new(request):
    form = GamesForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "Jogo cadastrado com sucesso" )
        form.save()
        return redirect('games_list')
    return render(request, 'jogos_form.html', {'form': form})

@login_required
def games_update(request,id):
    games = get_object_or_404(Games, pk=id)
    form = GamesForm(request.POST or None, instance=games)
    if form.is_valid():
        messages.success(request, "Jogo atualizado com sucesso" )
        form.save()
        return redirect('games_list')
    return render(request, 'jogos_form.html', {'form': form})

@login_required
def games_delete(request,id):
    game = get_object_or_404(Games, pk=id)
    if request.method == 'POST':
        messages.error(request, "Jogo deletado com sucesso" )
        game.delete()
        return redirect('games_list')
    return render(request, 'jogos_delete.html',{'delete':game})