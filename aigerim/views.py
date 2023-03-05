from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Добавить", 'url_name': 'add_post'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
def index(request): #HttpRequest
    posts = Aigerim.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'aigerim/index.html', context=context)

def about(request): #HttpRequest
    return render(request, 'aigerim/about.html', {'menu': menu, 'title': 'О нас'})

def addpage(requeat):
    return HttpResponse("Добавить")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    post = get_object_or_404(Aigerim, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'name': post.name,
        'cat_selected': post.cat_id,
    }
    return render(request, 'aigerim/post.html', context=context)

def show_category(request,cat_id):
    posts = Aigerim.objects.filter(cat_id=cat_id)

    if len(posts)  == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }
    return render(request, 'aigerim/index.html', context=context)
