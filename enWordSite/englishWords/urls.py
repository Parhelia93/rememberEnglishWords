from django.urls import path
from englishWords.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('categories/<slug:catId>', categories, name='cat'),
    path('partOfSpeech/<slug:speechPart>', partOfSpeech),
    path('about/', about, name='about'),
    path('addcat/', addcat, name='add_cat'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('progressCategory/<int:progCat>',progressCategory,name='progCat'),
    path('addWord',addWord, name='addword'),
]