from django.conf import settings

from users.models import User
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    discription = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.discription}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    discription = models.TextField(max_length=200, verbose_name='Описание продукта')
    picture = models.ImageField(upload_to='pics/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='категория продукта')
    price_for_buy = models.IntegerField(verbose_name='цена за покупку')
    data_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, blank=True,
                                              verbose_name='дата последнего изменения')  # c установкой при изменении
    phone = models.CharField(max_length=11, verbose_name='Телефон', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='user')

    def __str__(self):
        return f'{self.name}{self.discription}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    # product = models.ManyToManyField(Product, related_name='versions', blank=True)
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, **NULLABLE)
    number_version = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    flag_of_the_current_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
