from django.db import models


# Create your models here.
class Pessoa(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=30)
    apelido = models.CharField(max_length=40)
    def __str__(self):
        return "%s %s" % (self.nome, self.apelido)


class Tarefa(models.Model):
    nome = models.CharField(max_length=10)
    pessoa = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return "%s (%s %s)" % (self.nome, self.pessoa.nome, self.pessoa.apelido)
#x = dados.models.Pessoa.objects.all() - Selecionar tudo
#x = dados.models.Pessoa.objects.filter(nome="Chico") - Selecionar com o nome Chico
#x = dados.models.Pessoa.objects.filter(numero__gte=2) - Selecionar com o numero maior e igual a 2
#x = dados.models.Pessoa.objects.filter(numero__gte=2, nome="Chico")  - Selecionar com o numero maior e igual a 2 e com o nome Chico
#x = dados.models.Pessoa.objects.filter(iexact="chico")  - Selecionar com o nome Chico sem distinguir maiusculas e minusculas