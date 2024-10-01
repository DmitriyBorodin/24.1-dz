from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment_list = [
            {"user": User.objects.filter(pk=1).get(),
             "paid_course": Course.objects.filter(pk=3).get(),
             "payment_sum": "99",
             "payment_type": "Cash", },

            {"user": User.objects.filter(pk=1).get(),
             "paid_lesson": Lesson.objects.filter(pk=5).get(),
             "payment_sum": "49",
             "payment_type": "Cash", },

            {"user": User.objects.filter(pk=2).get(),
             "paid_course": Course.objects.filter(pk=1).get(),
             "payment_sum": "119",
             "payment_type": "Transfer", },

            {"user": User.objects.filter(pk=3).get(),
             "paid_course": Course.objects.filter(pk=2).get(),
             "payment_sum": "299",
             "payment_type": "Transfer", }
        ]

        payments_for_create = []

        for payment_item in payment_list:
            payments_for_create.append(Payments(**payment_item))

        Payments.objects.bulk_create(payments_for_create)
