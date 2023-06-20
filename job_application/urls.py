# created this file manually for url path!!
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'), #index path and view func and name!!
    path('about/',views.about,name='about')
]