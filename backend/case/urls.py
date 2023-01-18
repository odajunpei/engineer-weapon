from django.urls import path, include
from . import views
app_name = 'case'

urlpatterns = [
    path('', views.CaseListView.as_view(), name='case_list'),
    path('mylist/', views.CaseMyListView.as_view(), name='case_mylist'),
    path('create', views.CaseCreateView.as_view(),
         name="case_create"),
    path('<int:pk>', views.CaseDetailView.as_view(),
         name="case_detail"),
    path('<int:pk>/update',
         views.CaseUpdateView.as_view(), name='case_update'),
    path('<int:pk>/delete',
         views.CaseDeleteView.as_view(), name='case_delete'),
    path('<int:pk>/detail/create', views.DetailCreateView.as_view(),
         name="detail_create"),
    path('detail/<int:pk>', views.DetailDetailView.as_view(), name="detail_detail"),
    path('detail/<int:pk>/update',
         views.DetailUpdateView.as_view(), name="detail_update"),
    path('detail/<int:pk>/delete',
         views.DetailDeleteView.as_view(), name="detail_delete"),
    path('shop/<int:pk>',
         views.ShopDetailView.as_view(), name="shop_list"),
]
