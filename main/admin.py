from django.contrib import admin

from main.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'price_for_buy', 'data_create', 'last_modified_date')
    list_filter = ('name', 'category', 'discription')
    # search_fields = ('first_name','last_name',)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'discription')
    #list_filter = ('name', 'category', 'description')
    # search_fields = ('first_name','last_name',)

