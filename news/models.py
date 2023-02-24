from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=150, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
    
