from django import forms
from .models import Category, Article
from django_summernote.widgets import SummernoteWidget


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('user', 'title', 'thumbnail', 'category', 'url1', 'url2',
                  'url3', 'body', 'release', 'order')
        widgets = {
            'category': forms.CheckboxSelectMultiple,
            'body': SummernoteWidget(),
        }
