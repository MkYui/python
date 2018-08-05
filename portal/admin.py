from django.contrib import admin

from django.contrib.admin.options import InlineModelAdmin


from .models import CatalogPortal
# Register your models here.
from ckeditor.widgets import CKEditorWidget

from django.forms import ModelForm
from django.utils.timezone import now





admin.site.register(CatalogPortal )
