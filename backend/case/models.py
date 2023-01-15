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


class Status(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Case(models.Model):
    user = models.ForeignKey(
        User, verbose_name="投稿者", related_name="case_user", on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField('案件名', max_length=30)
    body = models.TextField('説明', blank=True, null=True, max_length=1500)
    release = models.BooleanField(default=True, verbose_name='公開する')
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)
    status = models.ManyToManyField(
        Status, verbose_name="ステータス", related_name="case_status", null=True, blank=True
    )
    url1 = models.URLField('テストurl', null=True, blank=True)
    login_id = models.CharField(
        'テスト環境ログインID', null=True, blank=True, max_length=50)
    password = models.CharField(
        'テスト環境ログインパスワード', null=True, blank=True, max_length=100)
    shop = models.ForeignKey(
        Shop, verbose_name="取引先企業", related_name="case_shop", on_delete=models.PROTECT, null=True, blank=True)
    member = models.ManyToManyField(
        User, verbose_name="メンバー", related_name="case_member", null=True, blank=True
    )

    def __str__(self):
        return self.title


class Detail(models.Model):
    user = models.ForeignKey(
        User, verbose_name="投稿者", related_name="detail_user", on_delete=models.PROTECT, null=True, blank=True)
    case = models.ForeignKey(
        Case, verbose_name="案件名", related_name="detail_case", on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField('案件名', max_length=30)
    body = models.TextField('説明', blank=True, null=True, max_length=1500)
    role = models.CharField('役割', blank=True, null=True, max_length=10)
    status = models.ForeignKey(
        Status, verbose_name="ステータス", related_name="detail_status", on_delete=models.PROTECT, null=True, blank=True
    )
    release = models.BooleanField(default=True, verbose_name='公開する')
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title
