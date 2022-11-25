from rest_framework import generics, views

from hello.models import Helloer
from .serializers import HelloSerializer, MessageSerilizer
from .responses import Message
from django101.settings import settings


class HelloerList(generics.ListAPIView):
    queryset = Helloer.objects.all()
    serializer_class = HelloSerializer


class HelloerDetail(generics.RetrieveAPIView):
    queryset = Helloer.objects.all()
    serializer_class = HelloSerializer


class SayHello(views.APIView):
    def get(self, request: views.Request, pk: int):
        try:
            helloer = Helloer.objects.get(id=pk)
        except Helloer.DoesNotExist:
            return views.Response(
                "cannot find the given helloer",
                status=views.status.HTTP_404_NOT_FOUND,
            )

        ms = MessageSerilizer(
            Message(
                message=f"{helloer.name} say hello to {settings.SUBJECT}",
                name=f"{helloer.name} {helloer.family}",
                age=helloer.age,
            )
        )
        return views.Response(ms.data)
