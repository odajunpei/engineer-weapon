from django.contrib import admin

from article.models import *
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Like)
