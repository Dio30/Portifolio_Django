
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from jogos import urls as jogos_urls
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import register_request, login_request
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('jogos/', include(jogos_urls)),
    path('registrar/', register_request, name='cadastro'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)