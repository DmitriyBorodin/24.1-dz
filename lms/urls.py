from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.views import LessonViewSet, SubscriptionAPIView, \
    SubscriptionListAPIView

from lms.views import CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, CourseDestroyAPIView
from lms.apps import LmsConfig

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", LessonViewSet)

urlpatterns = [
    path("course/", CourseListAPIView.as_view(), name="course_view"),
    path("course/<int:pk>/", CourseRetrieveAPIView.as_view(), name="course_retrieve"),
    path("course/create/", CourseCreateAPIView.as_view(), name="course_create"),
    path("course/<int:pk>/delete/", CourseDestroyAPIView.as_view(), name="course_delete"),
    path("course/<int:pk>/update/", CourseUpdateAPIView.as_view(), name="course_update"),
    path("course/<int:pk>/subscribe/", SubscriptionAPIView.as_view(), name="course_subscribe"),
    path("subs/", SubscriptionListAPIView.as_view(), name="subs_list"),
]

urlpatterns += router.urls
