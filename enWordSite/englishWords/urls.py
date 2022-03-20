from django.urls import path
from englishWords.views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:catId>', categories),
    path('partOfSpeech/<slug:speechPart>', partOfSpeech),
    path('about/', about, name='about')
]