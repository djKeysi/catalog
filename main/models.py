from django.db import models


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
    discription = models.TextField(max_length=200, verbose_name='Описание')
    picture = models.ImageField(upload_to='picture/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_for_buy = models.IntegerField(verbose_name='цена за покупку')
    data_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, blank=True, verbose_name='дата последнего изменения')  # c установкой при изменении
    #created_at = models.CharField(max_length=100, verbose_name='Создание', null=True, blank=True)
    def __str__(self):
        return f'{self.name}{self.discription}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


