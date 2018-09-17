# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.files.storage import default_storage
from django.core.exceptions import ImproperlyConfigured
from importlib import import_module

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
__all__ = ['AbstractAttachment', 'Attachment', ]

from ckeditor.fields import RichTextField

class CatalogNews(models.Model):
    title = models.CharField(max_length=200)
    public_date = models.DateTimeField(blank=True, null=True)
    news_texts = RichTextUploadingField()


    def was_published_recently(self):
        return self.public_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

    def contents(self):
        return self.contentss

    def textn(self):
        return self.text_n

    def ntext(self):
        return self.news_texts
