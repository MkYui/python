from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CatalogNews, Comment
from django.views.generic import CreateView

class PostForm(forms.ModelForm):
    class Meta:
        model = CatalogNews
        fields = ('title',)


class PersonCreateView(CreateView):
    model = CatalogNews
    fields = ('title', 'news_texts',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = CatalogNews
        fields = ('title',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Save person'))

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class SearchNewsForm(forms.Form):
    Поиск = forms.CharField( required=False)
