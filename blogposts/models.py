from django.db import models


NULLABLE = {'blank':True,'null':True}

class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    picture = models.ImageField(upload_to='pics/', verbose_name='превью', **NULLABLE)
    data_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0,verbose_name='количество просмотров')




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'