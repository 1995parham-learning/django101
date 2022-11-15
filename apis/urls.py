from django.urls import path

from .views import HelloerList, HelloerDetail

urlpatterns = [
    path("<int:pk>/", HelloerDetail.as_view(), name="helloer_detail"),
    path("", HelloerList.as_view(), name="helloer_list"),
]
