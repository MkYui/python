# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta as tdelta
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
#Forms
from .forms import PersonForm, CommentForm, SearchNewsForm
#models
from . import models
from .models import CatalogNews, Comment
from accounts.models import Users
#REST
from . import serializers
from rest_framework import generics
from .serializers import NewsSerializer
from rest_framework import routers, serializers, viewsets

from search_views.views import SearchListView
from search_views.filters import BaseFilter

def news_index(request):

    list_news = CatalogNews.objects.order_by('-created_at').filter(published=True)
    paginator = Paginator(list_news, 2)

    page = request.GET.get('page')
    try:
        catalognews = paginator.page(page)
    except PageNotAnInteger:
        catalognews = paginator.page(1)
    except EmptyPage:
        catalognews = paginator.page(paginator.num_pages)

    context = {'page_header': 'CatalogNews page',
               'list_news': list_news,
               'catalognews': catalognews,
               }

    return render(request, 'news/index.html', context , {'catalognews': catalognews,})

def news_detail(request, slug ):#news_id):
    news_item = get_object_or_404(CatalogNews, slug=slug)#pk=news_id)
    context_object_name = 'categorys'
    context = {
        'page_header': news_item.title,

        'news_item': news_item,
    }

    return render(request, 'news/detail.html', context)

# page error
def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')

# add news

class PersonListView(ListView):
    model = CatalogNews
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = CatalogNews
    fields = ('title', 'news_texts',)
    success_url = reverse_lazy('person_list')


class PersonUpdateView(UpdateView):
    model = CatalogNews
    form_class = PersonForm
    template_name = 'news/person_update_form.html'
    success_url = reverse_lazy('person_list')
#add end
def add_comment_to_post(request, pk):
    post = get_object_or_404(CatalogNews, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('news_detail', news_id=post.pk)
    else:
        form = CommentForm()
    return render(request, 'news/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', pk=comment.post.pk)
#REST API
class ItemViewSet(viewsets.ModelViewSet):#(viewsets.ModelViewSet):
    queryset = CatalogNews.objects.all()
    serializer_class = NewsSerializer


#Search

class ActorsFilter(BaseFilter):
    search_fields = {
        "Поиск" : ["title", "news_texts"],

    }

class SearchView(SearchListView):
    model = CatalogNews
    template_name = "search_list.html"

    form_class = SearchNewsForm
    filter_class = ActorsFilter
