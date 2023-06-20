from django.contrib import admin
from .models import Form # import our db model!!

# Register your models here.

class FormAdmin(admin.ModelAdmin): # created to customize admin form!!
    list_display=('first_name','last_name','email') # def tup to display!!
    search_fields=('first_name','last_name','email') # search list!!
    list_filter=('date','occupation')
    ordering=('first_name',)
    readonly_fields=('occupation',)


admin.site.register(Form,FormAdmin) # register db model with site and form admin!!