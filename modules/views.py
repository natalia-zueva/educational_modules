from rest_framework import generics

from modules.models import Module
from modules.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания образовательного модуля """

    serializer_class = ModuleSerializer


class ModuleListAPIView(generics.ListAPIView):
    """ Контроллер для вывода списка модулей """

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра модуля """

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения модуля """

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления модуля """

    queryset = Module.objects.all()
