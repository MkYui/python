#from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Users
from django.contrib.auth.models import User

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.shortcuts import redirect

from django.core.files.storage import FileSystemStorage

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .forms import DocumentForm

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




##upload image
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():

            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'accounts/model_form_upload.html', {
        'form': form
    })
