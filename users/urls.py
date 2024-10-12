from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from lms.views import LessonViewSet

from lms.views import CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, CourseDestroyAPIView
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsViewSet, UserCreateAPIView

app_name = UsersConfig.name

router_payments = SimpleRouter()
router_payments.register("payments/", PaymentsViewSet)

router_users = SimpleRouter()
router_users.register("", UserViewSet)

urlpatterns = [
    # path('payments/', include('users.urls.router_payments)', namespace='payments')),
    # path('users/', include('users.urls.router_payments)', namespace='payments')),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

urlpatterns += router_users.urls
urlpatterns += router_payments.urls
