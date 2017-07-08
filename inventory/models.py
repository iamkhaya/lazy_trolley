from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
    """Model for products displayed on site"""
    class Meta:
        """pluralization"""
        verbose_name_plural = "products"

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        to_field='name',
    )
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        to_field='name',
    )

    barcode = models.IntegerField()
    size = models.IntegerField()
    size_units = models.CharField(max_length=200)
    quantity = models.IntegerField()
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image_1 = models.FileField(upload_to='images/products', default='images/products/image_1.jpg')
    image_2 = models.FileField(upload_to='images/products', default='images/products/image_2.jpg')
    image_3 = models.FileField(upload_to='images/products', default='images/products/image_3.jpg')
    image_4 = models.FileField(upload_to='images/products', default='images/products/image_4.jpg')
    image_5 = models.FileField(upload_to='images/products', default='images/products/image_5.jpg')
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')

    def __unicode__(self):
        return u'{0}'.format(self.name)


class ShopBranch(models.Model):
    """Model for shop branches"""
    class Meta:
        """pluralization"""
        verbose_name_plural = "shop Branches"

    parent_company = models.ForeignKey(
        'ShopHeadquaters',
        on_delete=models.CASCADE,
        to_field='company_name',
    )

    shop_id = models.IntegerField()
    name = models.CharField(max_length=200, unique=True)
    street_number = models.IntegerField()
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.IntegerField()
    website = models.URLField(max_length=200)
    email = models.EmailField()
    collect = models.BooleanField()
    deliver = models.BooleanField()
    date_created = models.DateField(auto_now=True)
    logo = models.FileField(upload_to='images/logos/', default='images/products/logo.jpg')
    created_by = models.CharField(max_length=200, default='admin')

    def __unicode__(self):
        return u'{0}, {1}'.format(self.parent_company, self.name)


class ShopHeadquaters(models.Model):
    """Model for shop headquaters"""
    class Meta:
        """pluralization"""
        verbose_name_plural = "shop Headquaters"

    company_name = models.CharField(max_length=200, unique=True)
    street_number = models.IntegerField()
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default='Zimbabwe')
    telephone = models.IntegerField()
    website = models.URLField(max_length=200)
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')

    def __unicode__(self):
        return u'{0}'.format(self.company_name)

class ShopCatalogue(models.Model):
    """Model for Shop Catalogue"""
    class Meta:
        """pluralization"""
        verbose_name_plural = "shop Catalogues"

    shop = models.ForeignKey(
        'ShopBranch',
        on_delete=models.CASCADE,
        to_field='name',
    )

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        to_field='name',
    )

    price = models.DecimalField(max_digits=7, decimal_places=2)
    special_price = models.DecimalField(max_digits=7, decimal_places=2)
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')


class Category(models.Model):
    """Model forcategories"""
    class Meta:
        """pluralization"""
        verbose_name_plural = "categories"

    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Brand(models.Model):
    """Model for Brands"""
    class Meta:
        """pluralization"""
        verbose_name_plural = "brands"

    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=200, default='admin')

    def __unicode__(self):
        return u'{0}'.format(self.name)
