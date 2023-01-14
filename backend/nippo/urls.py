from django.urls import path
from . import views

app_name = 'nippo'
urlpatterns = [
    path('', views.nippo, name='nippo_form'),
]
