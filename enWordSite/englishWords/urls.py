from django.urls import path
from englishWords.views import *

urlpatterns = [
    path('', index),
]