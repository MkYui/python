# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.files.storage import default_storage
from django.core.exceptions import ImproperlyConfigured
from importlib import import_module

from rest_framework import serializers

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
__all__ = ['AbstractAttachment', 'Attachment', ]



STATUS_CHOICES = (
    ('d', 'Опубликовать'),
    ('p', 'Редактировать'),
    ('w', 'Проверить'),
)
class Category(models.Model):
    name = models.CharField( max_length=64)

    def __str__(self):
        return self.name

class CatalogNews(models.Model):

    title = models.CharField(max_length=200)
    #public_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)#, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)#, null=True)

    slug = models.SlugField(max_length=100, unique=True, null=True)
    news_texts = RichTextUploadingField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='category_book')
    published = models.BooleanField(default=True)
    port = models.BooleanField(default=False)

    def was_published_recently(self):
        return self.public_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

    def contents(self):
        return self.contentss

    def slu(self):
        return self.slug
        
    def cre(self):
        return self.created_at

    def conup(self):
        return self.updated_at

    def textn(self):
        return self.text_n

    def ntext(self):
        return self.news_texts

class Comment(models.Model):
    post = models.ForeignKey('CatalogNews', on_delete=models.CASCADE, related_name='comments',default='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=200, default='comments')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
