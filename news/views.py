from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import DetailView, UpdateView
from questions.forms import QuestionsForm

def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = 'article'
