from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView
from .forms import QuestionsForm
from .models import Questions

def questions_adress(request):
    questions = Questions.objects.all()
    return render(request, 'questions/forum.html', {'question': questions})

class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'

class QuestionsUpdateView(UpdateView):
    model = Questions
    template_name = 'questions/questions.html'
    
    form_class = QuestionsForm
    
class QuestionsDeleteView(DeleteView):
    model = Questions
    template_name = 'questions/question_delete.html'
    success_url = '/questions/forum/'
    
    
    
    

def questions(request):
    error = ''
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена некорректно!'
    
    form = QuestionsForm()
    
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'questions/questions.html', data)
