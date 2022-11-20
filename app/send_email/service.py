from django.core.mail import send_mail
from .models import Contact
import secrets

def send_weekly_news():
    for contact in Contact.objects.all():
        send_mail(
        'Weekly news from Quick pass!',
        '''This week is Black friday week,
         visit our partners for discounts!
         If you need quick password visit you site!''',
        'quickpass@eclipso.email',
        [contact.email],
        fail_silently=False,
    )
        print("email"*5, contact.email)
    print("email was sent"*5)

def send_secret(user_email, description, secret):
    send_mail(
    f'{description}',
    f'I created password {secret} for {description}',
    'quickpass@eclipso.email',
    [user_email],
    fail_silently=False,
)

def generate_pass():
    password_length = 17
    genpassword = (secrets.token_urlsafe(password_length))
    return genpassword
