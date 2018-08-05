from django.contrib import admin

from django.contrib.admin.options import InlineModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.settings import summernote_config, get_attachment_model

from ckeditor.widgets import CKEditorWidget

from .models import CatalogNews

admin.site.register(CatalogNews)
