from django.db import models

class Celphone(models.Model):
    celphone_name = models.CharField(max_length=40)
    # celphoneid =models.FloatField()
    celphone_price = models.FloatField()
    celphone_brand = models.CharField(max_length=40)
    celphone_description = models.CharField(max_length=200, null=True, blank=True)


class blog(models.Model):
    blog_title = models.CharField(max_length=40)
    blog_description = models.CharField(max_length=200)
    blog_date = models.DateField(auto_now_add= True, null= True, blank=True)
    blog_author = models.CharField(max_length=40)
    

class user(models.Model):
    user_name = models.CharField(max_length=40)
    user_email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=50)
    user_id = models.CharField(max_length=40)
    user_role=models.CharField(max_length=40)