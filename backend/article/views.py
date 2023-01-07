from accounts.models import User, Profile
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from article.forms import CategoryForm, ArticleForm
from .models import Category, Article, Like
from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model
# from django.contrib.auth.decorators import login_required
# カテゴリ


class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/category_form.html"
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse_lazy("article:category_list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/category_form.html"
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse_lazy("article:category_list")


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "article/category_list.html"
    model = Category


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "article/category_detail.html"
    model = Category


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "article/category_delete_form.html"


# 記事


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "article/article_list.html"
    model = Article


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = "article/article_detail.html"
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/article_form.html"
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy("article:article_detail", kwargs={'pk': self.object.pk})


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/article_form.html"
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy("article:article_detail", kwargs={'pk': self.object.pk})


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "article/article_delete_form.html"
    model = Article


class ArticleMYListView(LoginRequiredMixin, ListView):
    template_name = "article/article_mylist.html"
    model = Article

# お気に入り


@login_required
def Like_add(request, article_id):
    article = Article.objects.get(id=article_id)
    user = request.user
    is_like = Like.objects.filter(article=article, user=user)
    if is_like.exists():
        is_like.delete()
    else:
        is_like.create(article=article, user=user, favorite=True)

    return redirect('article:article_detail', article.id)


class ArticleFavoriteListView(LoginRequiredMixin, ListView):
    template_name = "article/article_favorite.html"
    model = Like
