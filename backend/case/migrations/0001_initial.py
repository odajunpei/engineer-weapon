# Generated by Django 3.1.7 on 2023-01-14 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='案件名')),
                ('body', models.TextField(blank=True, max_length=1500, null=True, verbose_name='説明')),
                ('release', models.BooleanField(default=True, verbose_name='公開する')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('url1', models.URLField(blank=True, null=True, verbose_name='テストurl')),
                ('login_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='テスト環境ログインID')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='テスト環境ログインパスワード')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='案件名')),
                ('body', models.TextField(blank=True, max_length=1500, null=True, verbose_name='説明')),
                ('role', models.CharField(blank=True, max_length=10, null=True, verbose_name='役割')),
                ('release', models.BooleanField(default=True, verbose_name='公開する')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='detail_case', to='case.case', verbose_name='案件名')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='detail_status', to='case.status', verbose_name='ステータス')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='detail_user', to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='case_shop', to='case.shop', verbose_name='取引先企業'),
        ),
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.ManyToManyField(blank=True, null=True, related_name='case_status', to='case.Status', verbose_name='ステータス'),
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='case_user', to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
    ]
