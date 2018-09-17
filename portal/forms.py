from django import forms
from .models import Comment
#from tumblelog.models import Comment
from fluent_comments.forms import CompactLabelsCommentForm


from .models import CatalogPortal, Comment



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
