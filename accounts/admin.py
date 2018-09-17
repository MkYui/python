from django.contrib import admin
#from .models import UserProfiler
# Register your models here.
from .models import ProfileUsers
from .models import Users
#from .models import Person

#admin.site.register(Person)
admin.site.register(ProfileUsers)
admin.site.register(Users)
