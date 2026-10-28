from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path(
        "",
        views.lista_posts,
        name="lista_posts"
    ),

    path(
        "post/crear/",
        views.crear_post,
        name="crear_post"
    ),

    path(
        "post/<int:pk>/",
        views.detalle_post,
        name="detalle_post"
    ),

    path(
        "post/<int:pk>/editar/",
        views.editar_post,
        name="editar_post"
    ),

    path(
        "post/<int:pk>/eliminar/",
        views.eliminar_post,
        name="eliminar_post"
    ),
]