from django.urls import path

from modules.apps import ModulesConfig
from modules.views import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, ModuleUpdateAPIView, \
    ModuleDestroyAPIView

app_name = ModulesConfig.name

urlpatterns = [
    path('modules/create/', ModuleCreateAPIView.as_view(), name='module-create'),
    path('modules/', ModuleListAPIView.as_view(), name='module-list'),
    path('modules/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-get'),
    path('modules/update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module-update'),
    path('modules/delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module-delete'),
]
