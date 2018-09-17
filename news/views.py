# -*- coding: utf-8 -*-

#from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required

from .models import CatalogNews
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


def news_index(request):

    list_news = CatalogNews.objects.all()
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

    return render(request, 'news/index.html', context)

def news_detail(request, news_id):
    news_item = get_object_or_404(CatalogNews, pk=news_id)
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
