from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "titulo",
            "contenido",
            "categoria",
            "imagen",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del perfume",
                }
            ),

            "contenido": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Escribí tu reseña...",
                }
            ),

            "categoria": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "imagen": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }