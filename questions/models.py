from django.db import models


class Questions(models.Model):
    title = models.CharField('Тема' ,max_length=50, null=False)
    text = models.TextField('Текст', null=False)
    # date = models.DateTimeField('Дата публикации', blank=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/questions/forum/{self.id}'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'