#from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .models import ProfileUsers
from .models import Users
from django.contrib.auth.models import User
#from django.views.generic import UpdateView
#from .forms import PersonForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

def indexs(request):

    people = ProfileUsers.objects.filter(id=request.user.id)
    return render(request, "accounts/profile.html", {"people": people})

class BookForm(ModelForm):
    class Meta:
        model = Users
        fields = ['bio', 'birthday', ]

@login_required
def book_list(request, template_name='accounts/profile_list.html'):
    if request.user:#is_user:
        book = Users.objects.filter(id=request.user.id)
    else:
        book = Users.objects.filter()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

@login_required
def book_create(request, template_name='accounts/profile_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return redirect('books_fbv_user:book_list')
    return render(request, template_name, {'form':form})

@login_required
def book_update(request, pk, template_name='accounts/profile_form.html'):
    if request.user:#.is_superuser:
        book= get_object_or_404(Users, pk=pk)
    else:
        book= get_object_or_404(Users, pk=pk, user=request.user)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books_fbv_user:book_list')
    return render(request, template_name, {'form':form})

@login_required
def book_delete(request, pk, template_name='accounts/profile_confirm_delete.html'):
    if request.user.is_superuser:
        book= get_object_or_404(ProfileUsers, pk=pk)
    else:
        book= get_object_or_404(ProfileUsers, pk=pk, user=request.user)
    if request.method=='POST':
        book.delete()
        return redirect('books_fbv_user:book_list')
    return render(request, template_name, {'object':book})


###API
