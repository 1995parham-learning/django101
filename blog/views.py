from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def post_list(request: HttpRequest):
    # pagination with 3 posts per page
    paginator = Paginator(Post.published.all(), 3)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)

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
