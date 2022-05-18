from django.db import models

class Games(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_do_jogo = models.CharField(max_length=30)
    tipo_de_jogo = models.CharField(max_length=30)
    preço_do_jogo = models.DecimalField(max_digits=7, decimal_places=2)
    descrição_do_jogo = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome_do_jogo