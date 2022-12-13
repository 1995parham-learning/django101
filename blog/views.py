from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_detail(
    request: HttpRequest, year: int, month: int, day: int, post_slug: str
):
    post = get_object_or_404(
        Post.published,
        slug=post_slug,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
