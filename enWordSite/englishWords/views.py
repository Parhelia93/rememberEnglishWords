from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

#Create your views here.


def index(request):
    return HttpResponse('Main Page of application')

def categories(request, catId):
    if request.GET:
        print(request.GET)
        if request.GET['name'] == 'fuckOff':
            raise Http404()
        if request.GET['sname'] == '123':
            return redirect('home')
    return HttpResponse(f'Categories number {catId}')

def partOfSpeech(request, speechPart):
    return HttpResponse(f'Part of speech: {speechPart}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Stranitsa ne naidena')