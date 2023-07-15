from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=20)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=20)
    alumnos = models.ManyToManyField(Alumno)

    def __str__(self):
        return self.nombre


