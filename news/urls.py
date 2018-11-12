from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from .views import PersonListView, PersonCreateView, PersonUpdateView
from django.contrib.auth.decorators import login_required

from rest_framework import routers
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.news_index, name='news_index'),
    #url(r'^(?P<news_id>[\d+]+)$', views.news_detail, name='news_detail'),
    #url(r'^articles/(?P<slug>[-\w]+)/$', views.news_detail, name='news_detail'),
    url(r'^news/(?P<slug>[\w-]+)/$', views.news_detail, name='news_detail'),
	url(r'^summernote/', include('django_summernote.urls')),
    path('add/', PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('', PersonListView.as_view(), name='person_list'),

    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
