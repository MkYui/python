# -*- coding: utf-8 -*-
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    url(r'^(?P<portal_id>[\d+]+)$', views.portal_detail, name='portal_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
