# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView

from django.http import Http404, HttpResponse
#from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta as tdelta
from django.views.generic import TemplateView
#from django.http import HttpResponse
#Models

from news.models import CatalogNews, Comment
#from news.models import Comment

from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_protect

from django.template.context import RequestContext
##
import json
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.views import View

##
def home(request):

    list_portal = CatalogNews.objects.filter(port=True)
    #list_portal = CatalogNews.objects.all()
    #list_news = range(1, 1000)
    page = request.GET.get('page', 1)

    paginator = Paginator(list_portal, 2)
    try:
        catalogportal = paginator.page(page)
    except PageNotAnInteger:
        catalogportal = paginator.page(1)
    except EmptyPage:
        catalogportal = paginator.page(paginator.num_pages)

    context = {'page_header': 'CatalogNews page',
               'list_portal': list_portal,
               'catalogportal': catalogportal,
               }

    return render(request, 'portal/portal_home.html', context, {'catalogportal': catalogportal})

def portal_detail(request, portal_id):
    portal_item = get_object_or_404(CatalogNews, pk=portal_id)
    context = {
        'page_header': portal_item.title,

        'portal_item': portal_item,

    }
    return render(request, 'portal/detail_portal.html', context)
