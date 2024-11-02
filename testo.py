from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER

send_mail(
    subject=f"Курс 'заглушка' обновился!",
    message="Один из ваших курсов получил обновление",
    from_email=EMAIL_HOST_USER,
    recipient_list=['di-laim@mail.ru'],
)
