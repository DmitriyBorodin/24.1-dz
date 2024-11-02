from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_course_update_notification(course_name, email):
    send_mail(
        subject=f"Курс '{course_name}' обновился!",
        message="Один из ваших курсов получил обновление",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
    )
    # print(f"Письмо отправлено на почту {email}, про курс {course_name}")
