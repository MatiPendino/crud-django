from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages



# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    messages.success(request, "Cursos listados!")
    return render(request, "gestion-cursos.html", {"cursos": cursos})


def registrar_curso(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    creditos = request.POST["txtCreditos"]

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, "Curso registrado!")
    return redirect("http://www.facebook.com")

def eliminacion_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, "Curso eliminado!")

    return redirect("/")

def edicion_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editar_curso(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    creditos = request.POST["txtCreditos"]

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request, "Curso editado!")

    return redirect("/")