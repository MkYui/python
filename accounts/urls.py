from . import views
from django.urls import path, include

from django.conf.urls import url

app_name = 'books_fbv_user'
urlpatterns = [

    path('edits', views.book_list, name='book_list'),

    path('edit/<int:pk>', views.book_update, name='book_edit'),

    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
]
