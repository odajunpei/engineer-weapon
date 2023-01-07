from django.urls import path 
from . import views

app_name = 'contact'
urlpaeertns = [
  path('', views.index, name='index')
]