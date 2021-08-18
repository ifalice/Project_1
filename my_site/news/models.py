from django.db import models
from django.urls import reverse




class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(
        upload_to=r'photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_pablished = models.BooleanField(
        default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def my_func(self):
        return "Hello from model"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Список новостей"
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk':self.pk })



class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id':self.pk })
