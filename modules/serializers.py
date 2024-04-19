from rest_framework import serializers

from modules.models import Module


class ModuleSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Module """

    class Meta:
        model = Module
        fields = '__all__'
