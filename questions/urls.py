from django.urls import path
from .views import *


urlpatterns = [
    path('', questions, name='questions'),
    path('forum/', questions_adress, name='question_adress'),
    path('forum/<int:pk>', QuestionsDetailView.as_view(), name='questions-detail'),
    path('forum/<int:pk>/update', QuestionsUpdateView.as_view(), name='question-update'),
    path('forum/<int:pk>/delete', QuestionsDeleteView.as_view(), name='question-delete'),
    
]