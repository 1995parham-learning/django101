from rest_framework import serializers

from hello.models import Helloer


class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helloer
        fields = ("name", "family", "age")
