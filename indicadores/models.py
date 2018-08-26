from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    institute = models.CharField(max_length=500, blank=True)
    rol = models.CharField(max_length=50, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username


#Models for the tables Indicadores App

class Carrera(models.Model):

    nombre = models.TextField()
    jefe = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Desercion(models.Model):
    id_carrera = models.IntegerField()
    id_periodo = models.IntegerField()
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Eficiencia(models.Model):
    id_carrera = models.IntegerField()
    id_periodo = models.IntegerField()
    total = models.IntegerField()
    generacion = models.TextField()
    periodo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class EgresadosT(models.Model):
    id_carrera = models.IntegerField()
    id_periodo = models.IntegerField()
    total = models.IntegerField()
    generacion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Evidencias(models.Model):
    id_carrera = models.IntegerField()
    ciclo = models.TextField()
    archivo = models.TextField()
    nombre_original = models.TextField()
    admin = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Links(models.Model):
    url = models.TextField()
    caducidad = models.DateField()
    creado = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Materia(models.Model):
    id_carrera = models.IntegerField()
    id_periodo = models.IntegerField()
    nombre = models.TextField()
    admin = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Matricula(models.Model):

    periodo = models.TextField()
    total = models.IntegerField()
    admin = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Periodo(models.Model):
    periodo = models.TextField()
    admin = models.TextField()
    status = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Reprobacion(models.Model):
    id_carrera = models.IntegerField()
    id_periodo = models.IntegerField()
    totalRepro = models.IntegerField()
    totalMat = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Titulacion(models.Model):
    id_carrera = models.IntegerField()
    id_periodo = models.IntegerField()
    total = models.IntegerField()
    periodo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
