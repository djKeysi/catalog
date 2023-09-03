from django.db import models


class Category:
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=200)
    picture = models.ImageField(upload_to='picture/')
    category = models.ForeignKey(Category)
    price_for_buy = models.IntegerField()
    data_create= models.DateTimeField()
    last_modified_date = models.DateField()# c установкой при изменении





