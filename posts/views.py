from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Post
from .forms import PostForm
from django.db.models import Q


def lista_posts(request):
    posts = Post.objects.all()

    busqueda = request.GET.get("q", "").strip()
    categoria = request.GET.get("categoria", "").strip()

    if busqueda:
        posts = posts.filter(
            Q(titulo__icontains=busqueda) |
            Q(contenido__icontains=busqueda)
        )

    categorias_validas = [
        valor for valor, nombre in Post.CATEGORIAS
    ]

    if categoria in categorias_validas:
        posts = posts.filter(categoria=categoria)
    else:
        categoria = ""

    return render(
        request,
        "posts/lista_posts.html",
        {
            "posts": posts,
            "busqueda": busqueda,
            "categoria_actual": categoria,
            "categorias": Post.CATEGORIAS,
        }
    )

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        "posts/detalle_post.html",
        {"post": post}
    )

@login_required
def crear_post(request):
    if request.method == "POST":
        formulario = PostForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.autor = request.user
            post.save()

            return redirect(
                "posts:detalle_post",
                pk=post.pk
            )

    else:
        formulario = PostForm()

    return render(
        request,
        "posts/formulario_post.html",
        {
            "formulario": formulario,
            "accion": "Crear publicación",
        }
    )

@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.autor != request.user:
        raise PermissionDenied

    if request.method == "POST":
        formulario = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if formulario.is_valid():
            formulario.save()

            return redirect(
                "posts:detalle_post",
                pk=post.pk
            )

    else:
        formulario = PostForm(instance=post)

    return render(
        request,
        "posts/formulario_post.html",
        {
            "formulario": formulario,
            "accion": "Editar publicación",
        }
    )

@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.autor != request.user:
        raise PermissionDenied

    if request.method == "POST":
        post.delete()

        return redirect("posts:lista_posts")

    return render(
        request,
        "posts/confirmar_eliminar.html",
        {"post": post}
    )