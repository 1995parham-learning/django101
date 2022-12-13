from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post


def post_list(request: HttpRequest):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


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
