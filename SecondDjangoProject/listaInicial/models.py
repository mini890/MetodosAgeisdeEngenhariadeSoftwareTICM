from django.db import models

# Create your models here.
class ListaInicial(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=20)