
from re import I
import re
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, News
from .forms import NewsForm
from django.views.generic import ListView, DeleteView




class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_pablished = True)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk = self.kwargs['category_id'])
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'],is_pablished = True)

class ViewNews(DeleteView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'



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


def view_news(request, news_id):
    # news_item = News.objects.get(pk = news_id)
    news_item = get_object_or_404(News, pk = news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            news  = form.save()
            return redirect(news)
    else:
        form = NewsForm() 
    return render(request, 'news/add_news.html', {"form": form})
    