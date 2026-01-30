from __future__ import annotations

from django.http import HttpRequest, HttpResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Publicacion


def _seed_minimo() -> None:
    """
    Seed mínimo para que el proyecto funcione sin comandos extra.
    Se ejecuta solo si la tabla está vacía.
    """
    if Publicacion.objects.exists():
        return

    Publicacion.objects.bulk_create(
        [
            Publicacion(
                titulo="Primera publicación",
                resumen="Ejemplo de renderización dinámica con variables y filtros.",
                contenido="Contenido de ejemplo. Aquí se demostrará truncatewords, upper, date, etc.",
                publicado=True,
            ),
            Publicacion(
                titulo="Publicación oculta",
                resumen="No debe aparecer en listados porque publicado=False.",
                contenido="Contenido no visible en listados públicos.",
                publicado=False,
            ),
            Publicacion(
                titulo="Segunda publicación",
                resumen="Incluye condicionales y navegación con url tags.",
                contenido="Contenido de ejemplo para mostrar detalle y links.",
                publicado=True,
            ),
        ]
    )


def inicio(request: HttpRequest) -> HttpResponse:
    _seed_minimo()

    return render(
        request,
        "aplicacion1/inicio.html",
        {
            "titulo": "Inicio",
            "descripcion": "Contenido estático + dinámico con herencia, includes y control de templates.",
        },
    )


def publicaciones(request: HttpRequest) -> HttpResponse:
    _seed_minimo()

    items = Publicacion.objects.filter(publicado=True).only("id", "titulo", "resumen", "creado_en", "publicado")

    return render(
        request,
        "aplicacion1/publicaciones.html",
        {
            "titulo": "Publicaciones",
            "items": items,
            "hoy": "now",
        },
    )


def publicacion_detalle(request: HttpRequest, pk: int) -> HttpResponse:
    _seed_minimo()

    pub = get_object_or_404(Publicacion, pk=pk, publicado=True)

    return render(
        request,
        "aplicacion1/publicacion_detalle.html",
        {
            "titulo": pub.titulo,
            "pub": pub,
        },
    )


def ir_publicaciones(_: HttpRequest) -> HttpResponse:
    # Redirección desde vista
    return redirect("dinamico:publicaciones")


def forzar_404(_: HttpRequest) -> HttpResponse:
    # Manejo básico de errores (raise)
    raise Http404("Recurso no encontrado (forzado).")
