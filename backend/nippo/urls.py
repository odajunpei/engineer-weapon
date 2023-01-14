from django.urls import path
from . import views

app_name = 'nippo'
urlpatterns = [
    path('', views.nippo, name='nippo_form'),
    path('<int:pk>/update', views.update, name='nippo_update'),
    path('list', views.NippoListView.as_view(), name="nippo_list"),
    path('mylist', views.NippoMyListView.as_view(), name="nippo_mylist"),
    path('<int:pk>', views.NippoDetailView.as_view(), name="nippo_detail")
]
