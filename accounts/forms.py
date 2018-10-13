from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Users
from django.views.generic import CreateView
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm ):
    class Meta:

        model = Users
        #
        fields = ('avatar', )
