from django.db import models

# Create your models here.
from django.db import models

class Celphone(models.Model):
    name = models.CharField(max_length=40)
    id =models.FloatField(primary_key=True,)
    price = models.FloatField()
    brand = models.CharField(max_length=40)
    description = models.CharField(max_length=200, null=True, blank=True)


class Blog(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add= True, null= True, blank=True)
    author = models.CharField(max_length=40)
    

class Usuarios(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=50)
    id = models.FloatField(primary_key=True,)
    role=models.CharField(max_length=40)