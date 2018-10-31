from django.contrib import admin

from django.contrib.admin.options import InlineModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.settings import summernote_config, get_attachment_model

from ckeditor.widgets import CKEditorWidget

from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _

from .models import CatalogNews, Category, Comment

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

class ListCreate(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = u'Фильтр по созданию'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            (1, u'За сегодня'),
            (2, u'За 3 дня'),
            (3, u'За неделю')
        )

    def queryset(self, request, queryset):
        if self.value() == 1:
            queryset = queryset.filter(created_at=now() - timedelta(days=1))
        elif self.value() == 2:
            queryset = queryset.filter(created_at=now() - timedelta(days=3))
        elif self.value() == 3:
            queryset = queryset.filter(created_at=now() - timedelta(days=7))
        return queryset

class ListUpdate(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = u'Фильтр по обновлению'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            (1, u'За сегодня'),
            (2, u'За 3 дня'),
            (3, u'За неделю')
        )

    def queryset(self, request, queryset):
        if self.value() == 1:
            queryset = queryset.filter(updated_at=now() - timedelta(days=1))
        elif self.value() == 2:
            queryset = queryset.filter(updated_at=now() - timedelta(days=3))
        elif self.value() == 3:
            queryset = queryset.filter(updated_at=now() - timedelta(days=7))
        return queryset

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ( ListCreate, ListUpdate,)
admin.site.register(CatalogNews,  AuthorAdmin)

admin.site.register(Category)
admin.site.register(Comment)
