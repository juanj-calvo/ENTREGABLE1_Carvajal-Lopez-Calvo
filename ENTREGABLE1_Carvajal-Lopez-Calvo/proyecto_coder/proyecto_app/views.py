from cgi import print_exception
from django.shortcuts import render,redirect
from multiprocessing import context
from proyecto_app.models import Celphone , user , blog
from proyecto_app.forms import formulario_products , formulario_usuarios , formulario_blog

# Create your views here.

def create_product(request):

    if request.method == 'POST':
        form = formulario_products(request.POST)
        if form.is_valid():
            Celphone.objects.create(
                celphone_name = form.cleaned_data['celphone_name'],
                celphone_id = form.cleaned_data['celphone_id'],
                celphone_price = form.cleaned_data['celphone_price'],
                celphone_brand = form.cleaned_data['celphone_brand'],
                celphone_decription = form.cleaned_data['celphone_description']
            )
            return redirect(list_products)


    elif request.method == 'GET':
        form = formulario_products()
        context = {'form': form}
        return render(request,'new_product.html', context=context)



def create_usuario(request):

    if request.method == 'POST':
        form = formulario_usuarios(request.POST)
        if form.is_valid():
            user.objects.create(
                user_name = form.cleaned_data['user_name'],
                user_id = form.cleaned_data['user_id'],
                user_password = form.cleaned_data['user_password'],
                user_email = form.cleaned_data['Email'],
                
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
            blog.objects.create(
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
    product = Celphone.objects.filter(name__icontains=search)
    context = {'product': product}
    return render(request, 'search_product.html', context=context)


def search_usuario(request):
    search = request.GET['search']
    usuario = user.objects.filter(name__icontains=search)
    context = {'usuario': usuario}
    return render(request, 'search_usuario.html', context=context)


def search_blog(request):
    search = request.GET['search']
    Blog = blog.objects.filter(name__icontains=search)
    context = {'Blog': Blog}
    return render(request, 'search_blog.html', context=context)

def list_products(request):
    products = Celphone.objects.all() #Trae todos
    context = {
        'products':products
    }
    return render(request, 'products_list.html', context=context)

def home(request):
    return render(request, 'home.html', context={})

def lista_usuarios(request):
    usuarios = user.objects.all() #trae todo los usuarios
    context= {
        'usuarios':usuarios
    }
    return render(request,'usuarios_1.html',context=context)

def lista_blog(request):
    Blog = blog.objects.all()
    context= {
        'Blog':Blog
    }
    return render(request,'blog_1.html',context=context)