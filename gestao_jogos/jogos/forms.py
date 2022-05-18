from django.forms import ModelForm
from .models import Games

class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields =['nome_do_jogo', 'tipo_de_jogo', 'preço_do_jogo', 'descrição_do_jogo']