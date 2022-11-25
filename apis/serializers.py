from rest_framework import serializers

from hello.models import Helloer
from .responses import Message


class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helloer
        fields = ("name", "family", "age")


class MessageSerilizer(serializers.Serializer):
    message = serializers.CharField(max_length=1024)
    name = serializers.CharField(max_length=1024)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Message(**validated_data)

    def update(self, instance, validated_data):
        pass
