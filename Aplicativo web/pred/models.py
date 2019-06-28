from django.db import models

# Crear modelo para descripción
class Desc(models.Model):
    Titulo = models.CharField(max_length=200,primary_key=True)
    Texto = models.TextField()

    def __str__(self):
        return self.Titulo

# Modelo para la descripción de las variables
class Cult(models.Model):
    Titulo = models.CharField(max_length=200)
    Variedad = models.TextField()
    Clima = models.TextField(default=" ")
    Fert = models.TextField(default=" ")
    Suelo = models.TextField(default=" ")
    Expo = models.TextField(default=" ")

    def __str__(self):
        return self.Titulo

# Modelo para formulario de ingreso

class Datos(models.Model):
    Titulo = models.CharField(max_length=200)
    P_accu = models.DecimalField(max_digits=6, decimal_places=2)
    T_avg_prev = models.DecimalField(max_digits=6, decimal_places=2)
    Rad_accu_prev1 = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.Titulo
