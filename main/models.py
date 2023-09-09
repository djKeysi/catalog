from django.db import models

NULLABLE = {'blank':True,'null':True}

# class Students(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Наименование')
#     discription = models.TextField(verbose_name='Описание')
#
#     def __str__(self):
#         return f'{self.name} {self.discription}'
#
#     class Meta:
#         verbose_name = 'категория'
#         verbose_name_plural = 'категории'



class Student(models.Model):
    first_name=models.CharField(max_length=100, verbose_name='имя')
    last_name=models.CharField(max_length=100, verbose_name='фамилия')
    avatar=models.ImageField(upload_to='students/',verbose_name='аватар',**NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)



