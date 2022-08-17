"""proyecto_coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from proyecto_coder.views import prueba_1
from proyecto_app.views import create_product, create_usuario ,create_blog, search_product , search_usuario , search_blog, lista_usuarios, lista_productos,lista_blog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba-1/',prueba_1,name= 'prueba_1'),
    path('create-product/',create_product,name='create_product'),
    path('create-usuario/', create_usuario, name= 'create_usuario'),
    path('create-blog/',create_blog, name= 'create_blog'),
    path('search-product/',search_product, name= 'search_product'),
    path('search-usuario/', search_usuario, name= 'search_usuario'),
    path('search-blog/',search_blog, name= 'search_blog'),
    path('lista_productos/',lista_productos, name= 'lista_productos'),
    path('lista_usuarios/', lista_usuarios, name= 'lista_usuarios'),
    path('lista_blog/',lista_blog, name= 'lista_blog'),
]
