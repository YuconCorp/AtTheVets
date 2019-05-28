from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.


class Factuur(models.Model):
    factuur_id = models.CharField(max_length=15, primary_key=True)
    factuur_datum = models.DateTimeField(default=timezone.now)
    factuur_beschrijving = models.CharField(max_length=50)
    factuur_bedrag = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    factuur_totaal = models.DecimalField(default=0, max_digits=15, decimal_places=2)


class Declaratie(models.Model):
    declaratie_id = models.CharField(max_length=15)
    declaratie_gedeclareerd = models.NullBooleanField(default='NULL')
    declaratie_retour = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    declaratie_totaal = models.DecimalField(default=0, max_digits=15, decimal_places=2)

    # def factuur(self):
    #    self.factuur_datum = timezone.now()
    #    self.save()

    #def __str__(self):
    #    return self.declaratie_id
