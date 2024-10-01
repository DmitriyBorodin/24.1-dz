from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.views import LessonViewSet

from lms.views import CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, CourseDestroyAPIView
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsViewSet

app_name = UsersConfig.name

router_payments = SimpleRouter()
router_payments.register("payments/", PaymentsViewSet)

router_users = SimpleRouter()
router_users.register("", UserViewSet)

urlpatterns = [

]

urlpatterns += router_users.urls
urlpatterns += router_payments.urls
