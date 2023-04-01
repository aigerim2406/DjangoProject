from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *

menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Добавить", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

class AigerimHome(DataMixin, ListView):
    model = Aigerim
    template_name = 'aigerim/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    contact_list = Aigerim.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'aigerim/about.html', {'page_obj': page_obj, 'menu': menu, 'title': "our_about"})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'aigerim/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить')
        return dict(list(context.items()) + list(c_def.items()))

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('aigerim/404_page.html')

class ShowPost(DataMixin, DetailView):
    model = Aigerim
    template_name = 'aigerim/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class AigerimCategory(DataMixin, ListView):
    model = Aigerim
    template_name = 'aigerim/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Aigerim.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Категории - ' + str(context['posts'][0].cat),
                                      cat_selected = context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))




# def show_post(request, post_slug):
#     post = get_object_or_404(Aigerim, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'name': post.name,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'aigerim/post.html', context=context)

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES )
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'aigerim/addpage.html', {'form': form, 'menu': menu, 'title': "Добавить"})

# def show_category(request,cat_id):
#     posts = Aigerim.objects.filter(cat_id=cat_id)
#
#     if len(posts)  == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'aigerim/index.html', context=context)

# def index(request):
#     posts = Aigerim.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu':  menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'aigerim/index.html', context=context)
