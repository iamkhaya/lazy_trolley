from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
    product_id = models.IntegerField()
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    size = models.IntegerField()
    size_units = models.CharField(max_length=200)
    quantity = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_1 = models.FileField(upload_to='images/products', default='images/products/image_1.jpg')
    image_2 = models.FileField(upload_to='images/products', default='images/products/image_2.jpg')
    image_3 = models.FileField(upload_to='images/products', default='images/products/image_3.jpg')
    image_4 = models.FileField(upload_to='images/products', default='images/products/image_4.jpg')
    image_5 = models.FileField(upload_to='images/products', default='images/products/image_5.jpg')
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')


class ShopBranches(models.Model):
    shop_id = models.IntegerField()
    name = models.CharField(max_length=200)
    parent_company = models.CharField(max_length=200)
    street_number = models.IntegerField()
    street1 =  models.CharField(max_length=200)
    street2 =  models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region =  models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.IntegerField()
    website = models.URLField(max_length=200)
    email = models.EmailField()
    collect = models.BooleanField()
    deliver = models.BooleanField()
    date_created = models.DateField(auto_now=True)
    logo = models.FileField(upload_to='images/logos/', default='images/products/logo.jpg')
    created_by = models.CharField(max_length=200, default='admin')


class ShopHeadquaters(models.Model):
    shop_headquaters_id = models.IntegerField()
    company_name = models.CharField(max_length=200)
    street_number = models.IntegerField()
    street1 =  models.CharField(max_length=200)
    street2 =  models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region =  models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.IntegerField()
    website = models.URLField(max_length=200)
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')

class ShopCatalogue(models.Model):
    shop_id = models.IntegerField()
    product_id = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')

class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')
