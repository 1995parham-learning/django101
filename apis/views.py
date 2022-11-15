from rest_framework import generics

from hello.models import Helloer
from .serializers import HelloSerializer


class HelloerList(generics.ListAPIView):
    queryset = Helloer.objects.all()
    serializer_class = HelloSerializer


class HelloerDetail(generics.RetrieveAPIView):
    queryset = Helloer.objects.all()
    serializer_class = HelloSerializer
