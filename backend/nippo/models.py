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


class Nippo(models.Model):
    user = models.ForeignKey(
        User, verbose_name="投稿者", related_name="nippo_user", on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(blank=False, null=False, max_length=200)
    date = models.DateTimeField('日付', default=timezone.now)
    created_at = models.DateTimeField('投稿日', default=timezone.now)
    updated_at = models.DateTimeField('更新日')

    def __str__(self):
        return self.title

class Time(models.Model):
  time = models.CharField(verbose_name="時間", max_length=30)

  def __str__(self):
        return self.time


class NippoDetail(models.Model):
    nippo = models.ForeignKey(
        Nippo, verbose_name="日報詳細", related_name="nippo_detail", on_delete=models.CASCADE, null=True, blank=True)
    plan = models.TextField(blank=True, null=True)
    actual = models.TextField(blank=True, null=True)
    time = models.ForeignKey(
        Time, verbose_name="時間", related_name="nippo_detail_time", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.plan