from django.contrib import admin
from .models import Games

class GamesAdmin(admin.ModelAdmin):
    readonly_fields = ('criado_por', )
    list_display = ('nome_do_jogo', 'tipo_de_jogo', 'preço_do_jogo')
    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.criado_por = usuario
        super(GamesAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(GamesAdmin, self).get_queryset(request)
        qs = qs.filter(criado_por=request.user)
        return qs
    
admin.site.register(Games, GamesAdmin)