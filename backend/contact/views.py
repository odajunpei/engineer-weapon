from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 追記
            username = form.cleaned_data['username']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            tel = form.cleaned_data['tel']
            sender = form.cleaned_data['sender']
            recipients = [settings.EMAIL_HOST_USER]
            # recipients_user = sender
            recipients.append(sender)
            try:
                ctx = {
                    "subject": subject,
                    "username": username,
                    "tel": tel,
                    "message": message,
                    "sender": sender
                }
                msg = render_to_string(
                    f"{settings.BASE_DIR}/contact/templates/mails/user.txt", ctx, request)
                send_mail(subject, msg, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('contact:complete')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})


def complete(request):
    return render(request, 'contact/complete.html')
