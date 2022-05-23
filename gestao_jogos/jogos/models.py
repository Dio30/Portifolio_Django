from django.contrib.auth.models import User
from django.db import models

class Games(models.Model):
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome_do_jogo = models.CharField(max_length=30)
    tipo_de_jogo = models.CharField(max_length=30)
    preço_do_jogo = models.DecimalField(max_digits=7, decimal_places=2)
    descrição_do_jogo = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Jogos'
        ordering = ['nome_do_jogo',]
    
    def __str__(self):
        return self.nome_do_jogo