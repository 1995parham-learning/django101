from django.urls import path

from .views import HelloerAPIView

urlpatterns = [path("", HelloerAPIView.as_view(), name="helloer_list")]
