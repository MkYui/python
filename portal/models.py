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

class CatalogPortal(models.Model):

    title = models.CharField(max_length=200)
    public_date = models.DateTimeField(blank=True, null=True)
    portal_texts = RichTextUploadingField()

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def was_published_recently(self):
        return self.public_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title


    def ntext(self):
        return self.portal_texts
