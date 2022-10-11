from django.db import models

# Create your models here.


class Coordonnees(models.Model):
    emplacement = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=30, decimal_places=20)
    longitude = models.DecimalField(max_digits=30, decimal_places=20)

    def __str__(self):
        return f"Les coordonnées de {self.emplacement} sont {self.latitude} et {self.longitude}"
