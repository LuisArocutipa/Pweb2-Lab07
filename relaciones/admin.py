from django.contrib import admin
from .models import Autor, Libro, Alumno, Asignatura

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Alumno)
admin.site.register(Asignatura)