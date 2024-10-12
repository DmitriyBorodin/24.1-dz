from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payments
from users.permissions import IsSameUser
from users.serializer import UserSerializer, PaymentsSerializer, \
    AnotherUserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer if IsSameUser else AnotherUserSerializer
    print(IsSameUser)

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            self.permission_classes = (IsSameUser,)
        return super().get_permissions()

    # def get_serializer_class(self):
    #     if self.kwargs.get('pk') == self.request.user.pk:
    #         return UserSerializer
    #     else:
    #         return AnotherUserSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["paid_course", "paid_lesson", "payment_type",]
    ordering_fields = ["payment_date", "payment_sum",]

    serializer_class = PaymentsSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
