# -*- coding: utf-8 -*-
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^(?P<portal_id>[\d+]+)$', views.portal_detail, name='portal_detail'),

    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#url(r'^post/(?P<portal_id>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
