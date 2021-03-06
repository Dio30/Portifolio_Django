from django.db import models
from usuarios.models import Cliente

class Games(models.Model):
    nome_do_jogo = models.CharField(max_length=30)
    tipo_de_jogo = models.CharField(max_length=30)
    preço_do_jogo = models.DecimalField(max_digits=7, decimal_places=2)
    descrição_do_jogo = models.TextField(null=True, blank=True)
    criado_por = models.ForeignKey(Cliente, on_delete= models.DO_NOTHING, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Jogos'
        ordering = ['nome_do_jogo',]
        
    def __str__(self):
        return self.nome_do_jogo