from django import forms

class formulario_products(forms.Form):

    name = forms.CharField(max_length=50)
    id = forms.FloatField()
    price = forms.FloatField()
    brand = forms.CharField(max_length=200)
    description = forms.CharField(max_length=400)


class fomulario_usuarios(forms.Form):

    name = forms.CharField(max_length=50)
    password = forms.IntegerField()
    id = forms.CharField(max_length=40)
    email = forms.CharField(max_length= 60)

class formulario_blog(forms.Form):

    title = forms.CharField(max_length= 60)
    autor = forms.CharField(max_length= 40)
    description = forms.CharField(max_length=600)
    date = forms.DateField()
