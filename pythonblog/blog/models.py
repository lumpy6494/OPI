from django.db import models
from django.urls import reverse

'''
Category 
=========

title, slug 


Tag 
=========
title, slug 


Post
==========
title, slug, content, created_at, photo, views,category, tags, author

'''

class Category(models.Model):
    title = models.CharField(max_length= 255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category',  kwargs={"slug": self.slug})



class Tag(models.Model):
    title = models.CharField(max_length=55, verbose_name='Тэг')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL Тэга')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('tag',  kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Пост')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL Поста')
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name = 'Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name= 'Фото')
    views = models.IntegerField(default=0, verbose_name='Колличество просмотров')
    category = models.ForeignKey(Category, models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name= 'Тэг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
