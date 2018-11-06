from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from django.test import TestCase
from .views import *

class PaginaInicial(TestCase):
    def test_pagina_inicial(self):
        resultado = resolve('/')
        self.assertEqual(resultado, paginaInicial)