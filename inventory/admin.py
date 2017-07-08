from django.contrib import admin

from .models import Product
from .models import ShopBranch
from .models import ShopCatalogue
from .models import ShopHeadquaters
from .models import Category
from .models import Brand


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'description', 'image_1']

class ShopBranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_company', 'city', 'telephone']

class ShopHeadquatersAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'city', 'region', 'telephone']

class ShopCatalogueAdmin(admin.ModelAdmin):
    list_display = ['shop_id', 'product_id', 'price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.register(ShopBranch, ShopBranchAdmin)
admin.site.register(ShopHeadquaters, ShopHeadquatersAdmin)
admin.site.register(ShopCatalogue, ShopCatalogueAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
