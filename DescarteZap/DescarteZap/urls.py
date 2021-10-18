"""DescarteZap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from paginas import views
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate


urlpatterns = {
    path('admin/', admin.site.urls),
    path('registrar/', UsuarioCreate.as_views(), name='registrar'),
    path('login/', auth_views.login_user.as_views(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_user.as_views, name='logout'),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', views.index),
    path('', include('paginas.urls')),
}
