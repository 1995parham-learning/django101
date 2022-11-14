from django.views import generic

from .models import Helloer


class HelloerListView(generic.ListView):
    model = Helloer
    template_name = "list.html"
