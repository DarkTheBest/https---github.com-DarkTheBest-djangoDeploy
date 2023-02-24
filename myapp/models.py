from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сообщение пользователя"
        verbose_name_plural = "Сообщения пользователей"
        
class Rules(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Правило"
        verbose_name_plural = "Правила"
        
class ContentIndex(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контент"