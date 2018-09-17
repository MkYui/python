from . import views
from django.urls import path, include

from django.conf.urls import url

app_name = 'books_fbv_user'
urlpatterns = [

    path('edits', views.book_list, name='book_list'),
    path('new', views.book_create, name='book_new'),
    path('edit/<int:pk>', views.book_update, name='book_edit'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),

]
