from django.contrib import admin
from .models import Form # import our db model!!

# Register your models here.
admin.site.register(Form) # register db model with site