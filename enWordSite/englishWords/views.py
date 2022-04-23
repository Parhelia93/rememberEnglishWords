from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from englishWords.models import *


menu = [{'title':'About site', 'url_name':'about'},
        {'title':'Add category', 'url_name':'add_cat'},
        {'title':'Feedback', 'url_name':'feedback'},
        {'title':'Login', 'url_name':'login'}]


def index(request):
    categoryList = WordCategory.objects.all()

    context = {'menu': menu,

               'cat_selected': 0,
               'title': 'Main Page',
               'cats': categoryList}
    return render(request, 'englishWords/index.html', context=context)


def categories(request, catId):
    # if request.GET:
    #     print(request.GET)
    #     if request.GET['name'] == 'fuckOff':
    #         raise Http404()
    #     if request.GET['sname'] == '123':
    #         return redirect('home')
    # return HttpResponse(f'Categories number {catId}')
    post_info = WordCategory.objects.get(slug=catId)
    print(post_info)
    context = {'menu': menu,
               'post': post_info}

    return render(request, 'englishWords/post.html', context=context)


def partOfSpeech(request, speechPart):
    return HttpResponse(f'Part of speech: {speechPart}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Stranitsa ne naidena')

def about(request):
    return render(request, 'englishWords/about.html', {'menu': menu, 'title':'Main Page'})


def addcat(request):
    return HttpResponse('Add category')

def feedback(request):
    return HttpResponse('Feedback page')

def login(request):
    return HttpResponse('Login page')

def progressCategory(request, progCat):
    categoryList = WordCategory.objects.filter(progress_cat=progCat)


    context = {'menu': menu,

               'cat_selected': progCat,
               'title': 'Main Page',
               'cats': categoryList}

    return render(request, 'englishWords/index.html', context=context)

