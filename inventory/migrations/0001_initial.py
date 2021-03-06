# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('size', models.IntegerField()),
                ('size_units', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('name', models.IntegerField()),
                ('description', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.IntegerField()),
                ('parent_company', models.CharField(max_length=200)),
                ('street_number', models.IntegerField()),
                ('street1', models.CharField(max_length=200)),
                ('street2', models.CharField(max_length=200)),
                ('suburb', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('collect', models.BooleanField()),
                ('deliver', models.BooleanField()),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
