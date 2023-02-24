from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('contacts/submit_message', submit_message, name='submit_message'),
    path('rules/', rules, name='rules')   
]
