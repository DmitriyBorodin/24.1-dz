from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Тесты для CRUD функционала модели Lesson"""
    def setUp(self):
        self.user = User.objects.create(email="test1user@email.com")
        self.course = Course.objects.create(name="Python 101",
                                            description="База по питону",
                                            owner=self.user)
        self.lesson = Lesson.objects.create(name="Урок 1. Зачем питон?",
                                            description="Поясняем за питон",
                                            course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson-detail", args=(self.lesson.pk,))

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("lms:lesson-list")
        data = {
            "name": "lesson idk",
            "description": "desc idk",
        }

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_create_forbidden(self):
        url = reverse("lms:lesson-list")
        data = {
            "name": "lesson idk",
            "description": "desc https://www.youtube.com/ idk",
        }

        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

    def test_lesson_update(self):
        url = reverse("lms:lesson-detail", args=(self.lesson.pk,))
        data = {
            "name": "Java 101",
            "description": "База по джаве"
        }

        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"), "Java 101"
        )

    def test_lesson_delete(self):
        url = reverse("lms:lesson-detail", args=(self.lesson.pk,))

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("lms:lesson-list")

        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        data = response.json()
        result = {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': self.lesson.pk, 'description': self.lesson.description,
             'name': self.lesson.name, 'preview': None, 'course': self.lesson.course.pk,
             'owner': self.lesson.owner.pk}]}

        self.assertEqual(
            data, result
        )


class SubscriptionTestCase(APITestCase):
    """Тесты для модели Subscription"""
    def setUp(self):
        self.user_1 = User.objects.create(email="user_1@email.com")
        self.user_2 = User.objects.create(email="user_2@email.com")
        self.course_python = Course.objects.create(name="Python 101",
                                            description="База по питону")
        self.course_java = Course.objects.create(name="Java 201",
                                            description="Продвинутый курс по джаве")
        self.subscription_1 = Subscription.objects.create(
            subscription_user=self.user_1,
            subscription_course=self.course_python,
            is_subscription_active=True
        )

    def test_creating_subscription_unregistered(self):
        """Неавторизованный пользователь пытается подписаться на курс,
        кол-во подписок не изменилось (1 -> 1)"""
        url = reverse("lms:course_subscribe", kwargs={"pk": 11})
        response = self.client.post(url)

        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            Subscription.objects.all().count(), 1
        )

    def test_creating_subscription(self):
        """Авторизованный пользователь пытается подписаться на курс,
        кол-во подписок увеличилось на 1 (1 -> 2)"""
        self.client.force_authenticate(user=self.user_2)
        url = reverse("lms:course_subscribe", kwargs={"pk": 8})
        response = self.client.post(url)
        baza = Course.objects.all()
        # for c in baza:
        #     print(c.pk)
        # print(Course.objects.filter(pk=8).get().__dict__)
        # print(response.json())
        self.assertEqual(
            Subscription.objects.all().count(), 2
        )

    def test_deleting_subscription(self):
        """Авторизованный пользователь уже подписанный на курс отписывается,
        кол-во подписок уменьшилось на 1 (1 -> 0)"""
        self.client.force_authenticate(user=self.user_1)

        url = reverse("lms:course_subscribe", kwargs={"pk": 11})
        response = self.client.post(url)
        print(Course.objects.filter(pk=12).get().__dict__)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            Subscription.objects.all().count(), 0
        )
