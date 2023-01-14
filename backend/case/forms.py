from django import forms
from .models import Case, Detail
from django_summernote.widgets import SummernoteWidget


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = "__all__"
        widgets = {
            'body': SummernoteWidget(),
            'status': forms.CheckboxSelectMultiple,
        }


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ('status', 'title', 'body', 'release')
        widgets = {
            'body': SummernoteWidget(),
        }
