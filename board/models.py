
from django.db import models
class Ads(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Описание', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'



