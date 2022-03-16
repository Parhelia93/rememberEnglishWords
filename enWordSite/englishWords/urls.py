from django.urls import path
from englishWords.views import *

urlpatterns = [
    path('', index),
    path('categories/<int:catId>', categories),
    path('partOfSpeech/<slug:speechPart>', partOfSpeech),
]