from django.db import models
from django.urls import reverse

class Aigerim(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price = models.BigIntegerField(default=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute(self):
        return reverse('post', kwargs={'post_id':self.pk})

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

