from rest_framework import generics

from modules.models import Module
from modules.paginators import ModulePaginator
from modules.permissions import IsOwner
from modules.serializers import ModuleSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ModuleCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания образовательного модуля """

    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]


class ModuleListAPIView(generics.ListAPIView):
    """ Контроллер для вывода списка модулей """

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulePaginator


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра модуля """

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения модуля """

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления модуля """

    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
