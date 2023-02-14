from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Добавить", 'url_name': 'add_post'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
def index(request): #HttpRequest
    posts = Aigerim.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
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
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request,cat_id):
    posts = Aigerim.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts)  == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }
    return render(request, 'aigerim/index.html', context=context)
