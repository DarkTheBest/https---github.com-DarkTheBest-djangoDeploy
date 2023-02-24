from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Message, Rules, ContentIndex

def index(request):
    data = ContentIndex.objects.all() 
    return render(request, 'myapp/index.html', {'data': data})

def about(request):
    return render(request, 'myapp/about.html')

def contacts(request):
    return render(request, 'myapp/contacts.html')

def rules(request):
    rule = Rules.objects.all()
    return render(request, 'myapp/rules.html', {'rules': rule})

@csrf_protect
def submit_message(request):
    if request.method == 'POST':
        # Создаем новое сообщение на основе данных из POST-запроса
        message = Message()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.subject = request.POST.get('subject')
        message.message = request.POST.get('text')
        # Сохраняем сообщение в базе данных
        message.save()
        # Перенаправляем пользователя на страницу подтверждения отправки сообщения
        return render(request, 'myapp/submit_message.html')
    else:
        # Если запрос не POST, возвращаем страницу контактов
        return render(request, 'myapp/contact.html')