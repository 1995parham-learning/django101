from django.urls import path

from .views import HelloerList, HelloerDetail, SayHello

urlpatterns = [
    path("<int:pk>/", HelloerDetail.as_view(), name="helloer_detail"),
    path("<int:pk>/say", SayHello.as_view(), name="say_hello"),
    path("", HelloerList.as_view(), name="helloer_list"),
]
