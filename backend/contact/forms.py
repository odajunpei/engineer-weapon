from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(label='ユーザ名', max_length=100)
    subject = forms.CharField(label='件名', max_length=100)
    sender = forms.EmailField(label='Email', help_text='※ご確認の上、正しく入力してください。')
    tel = forms.IntegerField(label='電話番号')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
