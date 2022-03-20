from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from englishWords.models import *
#Create your views here.


menu = ['About site', 'Add category', 'Feedback', 'Sing in']

def index(request):
    categoryList = WordCategory.objects.all()
    return render(request, 'englishWords/index.html', {'menu': menu, 'title':'Main Page',
                                                       'cats':categoryList})

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

def about(request):
    return render(request, 'englishWords/about.html', {'menu': menu, 'title':'Main Page'})