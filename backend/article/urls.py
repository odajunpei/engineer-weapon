from django.urls import path, include
from . import views
app_name = 'article'

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create', views.CategoryCreateView.as_view(),
         name="category_create"),
    path('category/<int:pk>', views.CategoryDetailView.as_view(),
         name="category_detail"),
    path('category/<int:pk>/update',
         views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete',
         views.CategoryDeleteView.as_view(), name='category_delete'),
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('me', views.ArticleMYListView.as_view(), name="article_mylist"),
    path('create', views.ArticleCreateView.as_view(), name="article_create"),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/update', views.ArticleUpdateView.as_view(), name="article_update"),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name="article_delete"),
    path('like/<int:article_id>', views.Like_add, name='like_add'),
    path('favorite/', views.ArticleFavoriteListView.as_view(),
         name="article_favorite")
]
