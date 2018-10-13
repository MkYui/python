from django.contrib import admin

from django.contrib.admin.options import InlineModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.settings import summernote_config, get_attachment_model

from ckeditor.widgets import CKEditorWidget

from .models import CatalogNews, Category
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]

    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='p')
    make_published.allowed_permissions = ('publish',)

    def has_publish_permission(self, request):
        """Does the user have the publish permission?"""
        opts = self.opts
        codename = get_permission_codename('publish', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))
admin.site.register(CatalogNews, ArticleAdmin)
admin.site.register(Category)
