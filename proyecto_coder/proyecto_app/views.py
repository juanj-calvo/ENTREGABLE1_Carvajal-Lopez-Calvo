from cgi import print_exception
from django.shortcuts import render
from multiprocessing import context
from productos.model import Productos , Usuarios , Blog
from proyecto_app.forms import formulario_products , formulario_usuarios , formulario_blog

# Create your views here.

def create_product(request):

    if request.method == 'POST':
        form = formulario_products(request.POST)
        if form.is_valid():
            Productos.objects.create(
                name = form.cleaned_data['name'],
                id = form.cleaned_data['id'],
                price = form.cleaned_data['price'],
                brand = form.cleaned_data['brand'],
                decription = form.cleaned_data['description']
            )
            return redirect(lista_productos)


    elif request.method == 'GET':
        form = formulario_products()
        context = {'form': form}
        return render(request,'new_product.html', context=context)



def create_usuario(request):

    if request.method == 'POST':
        form = formulario_usuarios(request.POST)
        if form.is_valid():
            Usuarios.objects.create(
                name = form.cleaned_data['name'],
                id = form.cleaned_data['id'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['Email'],
                
            )
            return redirect(lista_usuarios)


    elif request.method == 'GET':
        form = formulario_usuarios()
        context = {'form': form}
        return render(request,'new_usuario.html', context=context)


def create_blog(request):

    if request.method == 'POST':
        form = formulario_blog(request.POST)
        if form.is_valid():
            Blog.objects.create(
                title = form.cleaned_data['title'],
                autor = form.cleaned_data['autor'],
                date = form.cleaned_data['date'],
                decription = form.cleaned_data['description']
            )
            return redirect(lista_blog)


    elif request.method == 'GET':
        form = formulario_blog()
        context = {'form': form}
        return render(request,'new_blog.html', context=context)


def search_product(request):
    search = request.GET['search']
    product = Productos.objects.filter(name__icontains=search)
    context = {'product': product}
    return render(request, 'search_product.html', context=context)