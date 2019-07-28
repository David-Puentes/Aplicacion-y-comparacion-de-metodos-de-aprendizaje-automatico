from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    P_accu = models.DecimalField(max_digits=6, decimal_places=2, help_text="Valores entre 17.9 - 348.6 [mms]")
    T_avg_prev = models.DecimalField(max_digits=6, decimal_places=2, help_text="Valores entre 22.74 - 27.81 [C]")
    Rad_accu_prev1 = models.DecimalField(max_digits=6, decimal_places=2, help_text="Valores entre 109.5 - 524.3 [µmol·m²s-1]")

    def __str__(self):
        return self.Titulo
