from django.urls import path
from . import views

app_name = "aplicacion1"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("publicaciones/", views.publicaciones, name="publicaciones"),
    path("publicaciones/<int:pk>/", views.publicacion_detalle, name="publicacion_detalle"),
    path("ir-publicaciones/", views.ir_publicaciones, name="ir_publicaciones"),
    path("forzar-404/", views.forzar_404, name="forzar_404"),
]