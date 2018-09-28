# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
from django.utils import timezone
from django.urls import reverse

import datetime
from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.core.files.storage import default_storage
from django.core.exceptions import ImproperlyConfigured
from importlib import import_module
# Create your models here.
from taggit.managers import TaggableManager

#from fluent_comments.moderation import moderate_model, comments_are_open, comments_are_moderated
#from fluent_comments.models import get_comments_for_model, CommentsRelation

from django.contrib.auth.models import User
from datetime import date

from django.urls import reverse

class CatalogPortal(models.Model):

    title = models.CharField(max_length=200)

    public_date = models.DateTimeField(blank=True, null=True)
    portal_texts = RichTextUploadingField()

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.public_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    post = models.ForeignKey('CatalogPortal', on_delete=models.CASCADE, related_name='comments',default='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=200, default='comments')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

#moderate_model(
#    CatalogPortal,

#)
