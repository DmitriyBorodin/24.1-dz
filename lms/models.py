from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    preview = models.ImageField(upload_to='lms/course_previews', blank=True, null=True, verbose_name="Превью")
    description = models.TextField(verbose_name="Описание курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    preview = models.ImageField(upload_to='lms/lesson_previews', blank=True, null=True, verbose_name="Превью")
    description = models.TextField(verbose_name="Описание урока")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="Курс", blank=True, null=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

