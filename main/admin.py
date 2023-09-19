from django.contrib import admin

from main.models import Product, Category, Version


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'price_for_buy', 'data_create', 'last_modified_date')
    list_filter = ('name', 'category', 'discription')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'discription')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product','number_version', 'name_version','flag_of_the_current_version')




