from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError
import os
import string
from PIL import Image
from django.conf import settings
from django.contrib.auth import get_user, get_user_model
User = get_user_model()


def check_event_name(value):
    for kigo in string.punctuation:
        if kigo in value:
            raise ValidationError('タイトル、スラッグに半角記号は使えません')


class Category(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField('カテゴリー', max_length=30, unique=True)
    slug = models.SlugField(
        'スラッグ', max_length=100, unique=True, null=True, validators=[check_event_name])
    body = models.TextField('説明', blank=True, null=True, max_length=1500)
    release = models.BooleanField(default=True, verbose_name='公開する')
    order = models.PositiveIntegerField(
        default=1, null=False, blank=False, verbose_name='表示順')

    def __str__(self):
        return self.title


class Article(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    category = models.ManyToManyField(
        Category, related_name="category", verbose_name='カテゴリ', blank=True, null=True)
    title = models.CharField('記事タイトル', max_length=80, null=True)
    thumbnail = models.ImageField(
        'サムネイル', upload_to="article/%Y/%m/%d", null=True, blank=False)
    url1 = models.URLField('参考ページ1', null=True, blank=True)
    url2 = models.URLField('参考ページ2', null=True, blank=True)
    url3 = models.URLField('参考ページ3', null=True, blank=True)
    body = models.TextField('本文', blank=True, null=True)
    release = models.BooleanField(default=True, verbose_name='公開する')
    order = models.PositiveIntegerField(
        default=1, null=False, blank=False, verbose_name='表示順')
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title


# お気に入り
class Like(models.Model):
    article = models.ForeignKey(
        Article, related_name="article", verbose_name="記事", on_delete=models.PROTECT)
    user = models.ForeignKey(
        User, related_name="user", verbose_name="お気に入りしたユーザー", on_delete=models.PROTECT)
    favorite = models.BooleanField(default=False, verbose_name='お気に入りに登録する')
