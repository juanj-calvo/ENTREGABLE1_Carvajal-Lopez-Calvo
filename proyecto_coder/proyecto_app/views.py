from cgi import print_exception
from django.shortcuts import render
from multiprocessing import context
from productos.model import Productos
from proyecto_app.forms import formulario_products

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


