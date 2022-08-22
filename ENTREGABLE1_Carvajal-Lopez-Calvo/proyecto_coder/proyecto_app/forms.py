from django import forms

class formulario_products(forms.Form):

    celphone_name = forms.CharField(max_length=50)
    celphone_id = forms.FloatField()
    celphone_price = forms.FloatField()
    celphone_brand = forms.CharField(max_length=200)
    celphone_description = forms.CharField(max_length=400)


class formulario_usuarios(forms.Form):

    user_name = forms.CharField(max_length=50)
    user_password = forms.IntegerField()
    user_id = forms.CharField(max_length=40)
    user_email = forms.CharField(max_length= 60)
    user_role = forms.CharField(max_length=60)

class formulario_blog(forms.Form):

    blog_title = forms.CharField(max_length= 60)
    blog_author = forms.CharField(max_length= 40)
    blog_description = forms.CharField(max_length=600)
    blog_date = forms.DateField()
