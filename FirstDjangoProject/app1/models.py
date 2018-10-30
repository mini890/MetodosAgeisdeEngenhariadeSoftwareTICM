from django.db import models

# Create your models here.
class AppDados(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    telefone = models.CharField(max_length=10, blank=True)