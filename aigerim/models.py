from django.db import models
from django.urls import reverse

class Aigerim(models.Model):
    objects = None
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    price = models.BigIntegerField(default=True, verbose_name="Цена")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name="Категории", related_name = 'get_postsAigerim.objects.count')

    def __str__(self):
        return self.name

    def get_absolute(self):
        return reverse('post', kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name = 'Известные бренды'
        verbose_name_plural = 'Известные бренды'
        ordering = ['name']

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

