from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def send_user_mail(to,template,subject,msg):
    template = get_template(template)
    content = template.render({
        'subject':subject,
        'msg': msg,
    })
    message = EmailMultiAlternatives(subject,"",settings.EMAIL_HOST_USER,[to])
    message.attach_alternative(content, 'text/html')
    message.send()