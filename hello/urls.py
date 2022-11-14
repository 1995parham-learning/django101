from django.urls import path

from .views import HelloerListView

urlpatterns = [path("", HelloerListView.as_view(), name="list")]
