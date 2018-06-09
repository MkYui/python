from django.contrib import admin
#from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from django.contrib.admin.options import InlineModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.settings import summernote_config, get_attachment_model
#from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget

from .models import CatalogNews

#class NewsAdmin(models,Models):
#    pass



# Register your models here.
#admin.site.register(CatalogNews, NewsAdmin)
admin.site.register(CatalogNews)
