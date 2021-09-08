from django import template

from news.models import Category

from django.db.models import Count,F

register = template.Library()


@register.simple_tag(name = 'get_list_categories')
def get_categories():
    return Category.objects.all()



@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(count_news = Count('news')).filter(count_news__gt = 0)
    categories = Category.objects.annotate(count_news = Count('news', filter = F('news__is_pablished') )).filter(count_news__gt = 0)

    return {"categories": categories}