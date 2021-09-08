
from re import I
import re
from django.core import paginator

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, News
from .forms import NewsForm, UserRegisterForm
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.contrib import messages

from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Успешно зарегистрирован')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
    
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})

def login(request):
    return render(request, 'news/login.html')

def test(request):
    objects = [1,2,3,4,5,6,7]
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})



class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}
    mixin_prop = 'hello world'
    paginate_by = 2

    

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_pablished = True).select_related('category')

class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk = self.kwargs['category_id'])
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'],is_pablished = True).select_related('category')

class ViewNews(DeleteView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    login_url = '/admin/'


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': "Список новостей",        
#     }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id) 
#     category = Category.objects.get(pk = category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk = news_id)
#     news_item = get_object_or_404(News, pk = news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})

# def add_news(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             news  = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm() 
#     return render(request, 'news/add_news.html', {"form": form})
    