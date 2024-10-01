from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Lesson, Course


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    amount_of_lessons = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_amount_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return Lesson.objects.filter(course=course).values("name", "description",)

    class Meta:
        model = Course
        fields = ("name", "description", "amount_of_lessons", "lessons",)
