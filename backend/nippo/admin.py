from django.contrib import admin
from nippo.models import *


class NippoDetailInline(admin.StackedInline):
    model = NippoDetail
    extra = 8


class NippoAdmin(admin.ModelAdmin):
    inlines = [NippoDetailInline]


admin.site.register(Nippo, NippoAdmin)
admin.site.register(NippoDetail)
admin.site.register(Time)
