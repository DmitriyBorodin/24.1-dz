# Generated by Django 5.1.2 on 2024-10-13 19:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_course_owner_lesson_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_subscription_active', models.BooleanField(verbose_name='Подписка активна')),
                ('subscription_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lms.course', verbose_name='Курс')),
                ('subscription_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]