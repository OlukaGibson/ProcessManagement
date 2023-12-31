from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PHASES = (
    ('SMT','SMT'),
    ('THT','THT'),
    ('tunning','tunning'),
    ('monitor assembly','monitor assembly'),
    ('communication config','communication config'),
    ('analysis','analysis'),
    ('correction','correction')
)


class Items (models.Model):
    item_code = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=100)
    despription = models.TextField(max_length=100)

class Stock(models.Model):
    item_name = models.CharField(max_length=100,null=True)
    stock_in  = models.PositiveIntegerField(null=True)
    stock_out  = models.PositiveIntegerField(null=True)
    inventory = models.PositiveIntegerField(null=True)
    units = models.CharField(max_length=100,null=True)
    edit_date = models.DateField(auto_now=True)
    edited_by = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    item_code = models.ForeignKey(Items,on_delete=models.CASCADE, default=104)
    

class Casing (models.Model):
    batch_number = models.CharField(max_length=100,null=True)
    device_name = models.CharField(max_length=100,null=True)
    quantity = models.PositiveIntegerField(null=True)
    date_start = models.DateField(auto_now=False,auto_now_add=False,)
    detail = models.CharField(max_length=1000,null=True)

class Production (models.Model):
    batch_number = models.CharField(max_length=100)
    phase = models.CharField(choices=PHASES,null=True)
    quantity_in = models.PositiveIntegerField(null=True)
    quantity_out = models.PositiveIntegerField(null=True)
    date_start = models.DateField(auto_now=False,auto_now_add=False)
    detail = models.CharField(max_length=1000,null=True)
