from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Main Page of application')

def categories(request, catId):
    return HttpResponse(f'Categories number {catId}')

def partOfSpeech(request, speechPart):
    return HttpResponse(f'Part of speech: {speechPart}')
