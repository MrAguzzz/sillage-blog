from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    CATEGORIAS = [
        ("disenador", "Diseñador"),
        ("arabe", "Árabe"),
        ("nicho", "Nicho"),
    ]

    titulo = models.CharField(max_length=200)

    contenido = models.TextField()

    imagen = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="publicaciones"
    )

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default="disenador"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo