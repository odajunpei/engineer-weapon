# from django import forms
# from .models import NippoDetail


# class NippoDetailCreateForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = NippoDetail
#         fields = ('title', 'plan', 'actual', 'date')


# # これがモデルフォームセット
# NippoDetailCreateFormSet = forms.modelformset_factory(
#     NippoDetail, form=NippoDetailCreateForm, extra=8
# )
