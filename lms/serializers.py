from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms.models import Lesson, Course, Subscription
from lms.validators import validate_description_links


class LessonSerializer(serializers.ModelSerializer):

    description = serializers.CharField(validators=[validate_description_links])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    description = serializers.CharField(validators=[validate_description_links])

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    amount_of_lessons = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_amount_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return Lesson.objects.filter(course=course).values("name", "description",)

    class Meta:
        model = Course
        fields = ("name", "description", "amount_of_lessons", "lessons",)


class SubscriptionSerializer(serializers.ModelSerializer):

    is_subscribed = SerializerMethodField()

    def get_is_subscribed(self, subscription):
        return subscription.is_subscription_active

    class Meta:
        model = Subscription
        fields = ("subscription_user", "subscription_course", "is_subscribed",)
