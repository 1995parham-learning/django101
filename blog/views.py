from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail
from .models import Post
from .forms import EmailPostForm


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


def post_share(request: HttpRequest, post_id: int):
    post = get_object_or_404(
        Post.objects,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )

            send_mail(subject, message, "parham.alvani@gmail.com", [cd["to"]])
    else:
        form = EmailPostForm()
    return render(
        request, "blog/post/share.html", {"post": post, "form": form}
    )
