from django.contrib import admin
from django.urls import path
from proyecto_app.views import create_product, create_usuario , create_blog, search_product , search_usuario , search_blog, list_products, home, lista_usuarios,lista_blog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-product/',create_product,name='create_product'),
    path('create-usuario/', create_usuario, name= 'create_usuario'),
    path('create-blog/',create_blog , name= 'create_blog'),
    path('search-product/',search_product, name= 'search_product'),
    path('search-usuario/', search_usuario, name= 'search_usuario'),
    path('search-blog/',search_blog, name= 'search_blog'),
    path('home/', home, name='home'),
    path('list-products/', list_products, name='list_products'),
    path('lista-usuarios/', lista_usuarios, name= 'lista_usuarios'),
    path('lista-blog/', lista_blog, name= 'lista_blog'),
]