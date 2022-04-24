from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import AddWordCategory

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
    word_list = post_info.word_cat.all()
    context = {'menu': menu,
               'cat_selected': post_info.progress_cat_id,
               'post': post_info,
               'word_cat': word_list}

    return render(request, 'englishWords/post.html', context=context)


def partOfSpeech(request, speechPart):
    return HttpResponse(f'Part of speech: {speechPart}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Stranitsa ne naidena')

def about(request):
    return render(request, 'englishWords/about.html', {'menu': menu, 'title':'Main Page'})


def addcat(request):
    if request.method == 'POST':
        add_cat_form = AddWordCategory(request.POST)
        if add_cat_form.is_valid():
            #print(add_cat_form.cleaned_data)
            try:
                WordCategory.objects.create(**add_cat_form.cleaned_data)
                return redirect('home')
            except:
                add_cat_form.add_error(None, 'Common Error Add Post')
    else:
        add_cat_form = AddWordCategory()

    context = {'menu': menu,
               'title': 'Add Page',
               'form': add_cat_form
               }
    return render(request, 'englishWords/addWordCat.html', context=context)

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

