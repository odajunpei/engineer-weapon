from django import forms
from .models import NippoDetail, Nippo


class NippoCreateForm(forms.ModelForm):
    class Meta:
        model = Nippo
        fields = ('title', 'date', 'updated_at')


class NippoDetailCreateForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = NippoDetail
        fields = ('plan', 'actual', 'time')

        widgets = {
            'plan': forms.Textarea(attrs={'rows': 4, 'cols': 10}),
            'actual': forms.Textarea(attrs={'rows': 4, 'cols': 10}),
        }


FileFormset = forms.inlineformset_factory(
    Nippo, NippoDetail, fields='__all__',
    extra=8, max_num=8, can_delete=False
)
