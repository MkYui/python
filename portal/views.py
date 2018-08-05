# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic.list import ListView


from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta as tdelta
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse

from .models import CatalogPortal
#from .models import Comments
from django.views.generic import ListView, DetailView

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404
from django.template.context import RequestContext

def home(request):

    list_portal = CatalogPortal.objects.all().order_by("-id")
    #list_news = range(1, 1000)
    page = request.GET.get('page', 1)

    paginator = Paginator(list_portal, 2)
    try:
        catalogportal = paginator.page(page)
    except PageNotAnInteger:
        catalogportal = paginator.page(1)
    except EmptyPage:
        catalogportal = paginator.page(paginator.num_pages)

    context = {'page_header': 'CatalogPortal page',
               'list_portal': list_portal,
               'catalogportal': catalogportal,
               }

    return render(request, 'portal/home.html', context, {'catalogportal': catalogportal})

def portal_detail(request, portal_id):
    portal_item = get_object_or_404(CatalogPortal, pk=portal_id)
    context = {
        'page_header': portal_item.title,

        'portal_item': portal_item,

    }
    return render(request, 'portal/detail_portal.html', context)

def add_comment_to_post(request, pk):
    portal_item = get_object_or_404(CatalogPortal, pk=portal_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = portal_item
            comment.save()
            return redirect('detail_portal', pk=portal_id)
    else:
        form = CommentForm()
    return render(request, 'portal/add_comment_to_post.html', {'form': form})
