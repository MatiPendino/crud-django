from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("registrarCurso/", views.registrar_curso),
    path("edicionCurso/<codigo>", views.edicion_curso),
    path("editarCurso/", views.editar_curso),
    path("eliminacionCurso/<codigo>", views.eliminacion_curso),
]