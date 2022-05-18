from django.urls import path
from .views import games_list
from .views import games_new
from .views import games_update
from .views import games_delete

urlpatterns = [
    path('lista/', games_list, name='games_list'),
    path('novo/', games_new, name='games_new'),
    path('atualizar-jogo/<int:id>', games_update, name='games_update'),
    path('delete/<int:id>', games_delete, name='games_delete')
]