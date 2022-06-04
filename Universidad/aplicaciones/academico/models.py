from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    creditos = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.codigo}, {self.nombre}, {self.creditos})"