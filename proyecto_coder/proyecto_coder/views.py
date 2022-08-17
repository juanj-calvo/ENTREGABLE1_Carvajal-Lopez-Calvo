from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def prueba_1(request):
    lista=[1,2,3,'hola mundo']
    context = {
        'prueba': 'otra prueba ',
        'lista': lista
    }
    return render(request,'prueba_1.html',context= context)
