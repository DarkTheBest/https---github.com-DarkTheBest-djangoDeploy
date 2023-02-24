from django.urls import path
from .views import *


urlpatterns = [
    path('', news_home, name='news_home'),
    path('<int:pk>', NewsDetailView.as_view(), name='news-detail'),
]
