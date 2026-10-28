from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "categoria",
        "fecha_creacion"
    )

    search_fields = (
        "titulo",
        "contenido"
    )

    list_filter = (
        "categoria",
        "fecha_creacion"
    )

    readonly_fields = (
        "fecha_creacion",
        "fecha_actualizacion"
    )