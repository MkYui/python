from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
import uuid

class ProfileUsers(models.Model):#:(AbstractUser)
    users = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    Names = models.CharField(max_length=20, default='DEFAULT VALUE')
    AboutMe = models.TextField(max_length=20, default='DEFAULT VALUE')
    email = models.EmailField(max_length=255,unique=True,)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username', 'full_name']

    #def __str__(self):
    #    return self.Names

    def get_absolute_url(self):
        return reverse('books_fbv_user:book_edit', kwargs={'pk': self.pk})

class Users(AbstractUser):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #users = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.CharField(max_length=160, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    AboutMe = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
