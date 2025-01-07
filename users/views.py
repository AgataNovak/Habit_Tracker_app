from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)

from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User

from .serializers import UserSerializer


class UserCreateApiView(CreateAPIView):
    """Контроллер создания объекта класса User"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListApiView(ListAPIView):
    """Контроллер просмотра списка объектов класса User"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра объекта класса User"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateApiView(UpdateAPIView):
    """Контроллер обновления объекта класса User"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyApiView(DestroyAPIView):
    """Контроллер удаления объекта класса User"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProfileViewSet(viewsets.ModelViewSet):
    """Контроллер операций с личным профилем авторизованного пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()
