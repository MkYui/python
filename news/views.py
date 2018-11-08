# -*- coding: utf-8 -*-

#from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required

from .models import CatalogNews
from .models import Comment
# Create your views here.

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

#from django.shortcuts import render
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta as tdelta
from django.views.generic import TemplateView
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView
from .forms import PersonForm

from django.contrib.auth.decorators import login_required
from . import models
from . import serializers
from rest_framework import generics

from .serializers import NewsSerializer
from rest_framework import routers, serializers, viewsets

from .forms import CommentForm

def news_index(request):

    list_news = CatalogNews.objects.order_by('-created_at')
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

def news_detail(request, news_id):
    news_item = get_object_or_404(CatalogNews, pk=news_id)
    context_object_name = 'categorys'
    context = {
        'page_header': news_item.title,

        'news_item': news_item,

    }

    return render(request, 'news/detail.html', context)

    #def get_object(self):
     #       return get_object_or_404(CatalogNews, slug__iexact=self.kwargs['slug'])
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
class ItemViewSet(viewsets.ModelViewSet):
    queryset = CatalogNews.objects.all()
    serializer_class = NewsSerializer
