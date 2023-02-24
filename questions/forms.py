from .models import Questions
from django.forms import ModelForm, TextInput, Textarea
class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['title','text']
        
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),         
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Задайте вопрос'
            }),
            # "date": DateInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Дата публикации'
            # }),
        }