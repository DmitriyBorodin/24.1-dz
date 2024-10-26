from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payments
from users.permissions import IsSameUser
from users.serializer import UserSerializer, PaymentsSerializer, \
    AnotherUserSerializer
from users.services import create_stripe_product, create_stripe_price, \
    create_stripe_session


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            self.permission_classes = (IsSameUser,)
        return super().get_permissions()

    # def get_serializer_class(self):

        # obj_pk = self.kwargs.get('pk')
        # user_pk = self.request.user.id

        # if int(obj_pk) == int(user_pk):
        #     return UserSerializer
        # else:
        #     return AnotherUserSerializer

        # if IsSameUser:
        #     return UserSerializer
        # else:
        #     return AnotherUserSerializer

        # print(type(self.kwargs.get('pk')))
        # print(type(self.request.user.id))
        #
        # print(f'obj_pk - {obj_pk}')
        # print(f'user_pk - {user_pk}')
        # print(obj_pk == user_pk)


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


class PaymentsCreateAPIView(CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        if payment.paid_course or payment.paid_lesson:
            product = payment.paid_course if payment.paid_lesson else payment.paid_lesson
            print(product)
            product_id = create_stripe_product(product)
            price = create_stripe_price(product_id, payment.payment_sum)
            session_id, payment_link = create_stripe_session(price)

            payment.session_id = session_id
            payment.link = payment_link
            payment.save()
        else:
            raise ValidationError("Выберите курс или урок для оплаты")


