from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from .views import PersonListView, PersonCreateView, PersonUpdateView

urlpatterns = [
    path('', views.news_index, name='news_index'),
    url(r'^(?P<news_id>[\d+]+)$', views.news_detail, name='news_detail'),
	url(r'^summernote/', include('django_summernote.urls')),
    path('add/', PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('', PersonListView.as_view(), name='person_list'),
    
##Api
    path('api/', views.NewsListApi.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
