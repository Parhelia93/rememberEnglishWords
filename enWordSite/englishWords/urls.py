from django.urls import path
from englishWords.views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:catId>', categories, name='cat'),
    path('partOfSpeech/<slug:speechPart>', partOfSpeech),
    path('about/', about, name='about'),
    path('addcat/', addcat, name='add_cat'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login')
]