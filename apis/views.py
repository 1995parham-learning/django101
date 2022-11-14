from rest_framework import generics

from hello.models import Helloer
from .serializers import HelloSerializer


class HelloerAPIView(generics.ListAPIView):
    queryset = Helloer.objects.all()
    serializer_class = HelloSerializer
