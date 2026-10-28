from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegistroForm

def registro(request):
    if request.user.is_authenticated:
        return redirect("posts:lista_posts")

    if request.method == "POST":
        formulario = RegistroForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()

            login(request, usuario)

            return redirect("posts:lista_posts")

    else:
        formulario = RegistroForm()

    return render(
        request,
        "usuarios/registro.html",
        {"formulario": formulario}
    )