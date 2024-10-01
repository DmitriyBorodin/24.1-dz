from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user_list = [
            {"email": "123@mail.com",
             "phone": "+123123123",
             "city": "МСК"},

            {"email": "456@mail.com",
             "phone": "+321321321",
             "city": "СПБ"},

            {"email": "12121212@mail.com",
             "phone": "+989898989",
             "city": "NY"},
        ]

        users_for_create = []

        for user_item in user_list:
            users_for_create.append(User(**user_item))

        User.objects.bulk_create(users_for_create)
