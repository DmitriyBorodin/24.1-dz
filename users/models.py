from django.contrib.auth.models import AbstractUser

from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Телефон')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватарка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Пользователь")
    payment_date = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Оплаченный курс")
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Оплаченный урок")
    payment_sum = models.PositiveIntegerField(verbose_name="Сумма оплаты")

    PAYMENT_TYPE_CHOICES = (
        ('Cash', 'Наличными'),
        ('Transfer', 'Перевод на счёт'),
    )
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
