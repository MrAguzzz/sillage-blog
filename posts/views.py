from django.shortcuts import render, get_object_or_404
from .models import Post


def lista_posts(request):
    posts = Post.objects.all()

    return render(
        request,
        "posts/lista_posts.html",
        {"posts": posts}
    )


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        "posts/detalle_post.html",
        {"post": post}
    )