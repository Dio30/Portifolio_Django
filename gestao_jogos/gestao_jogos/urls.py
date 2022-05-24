
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from jogos import urls as jogos_urls
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from usuarios import urls as usuarios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('jogos/', include(jogos_urls)),
    path('usuarios/', include(usuarios_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)