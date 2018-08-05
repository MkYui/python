# -*- coding: utf-8 -*-
"""news_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import fluent_comments.urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django_summernote.views import (
    SummernoteEditor, SummernoteUploadAttachment
)
from django.conf import global_settings

from django.views.static import serve
from portal import views

import django_comments.urls
COMMENT_URLS = django_comments.urls

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    path('', include('portal.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('redactor/', include('redactor.urls')),
    url(r'^editor/(?P<id>.+)/$', SummernoteEditor.as_view(),
        name='django_summernote-editor'),
    url(r'^upload_attachment/$', SummernoteUploadAttachment.as_view(),
        name='django_summernote-upload_attachment'),

    url(r'^blog/comments/', include('fluent_comments.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG is False:
    urlpatterns += [url(r'^media/(?P<path>.*)$',serve,{ 'document_root': settings.MEDIA_ROOT, }), ]

if settings.DEBUG is False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
