from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', views.news_index, name='news_index'),
    url(r'^(?P<news_id>[\d+]+)$', views.news_detail, name='news_detail'),
	url(r'^summernote/', include('django_summernote.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
