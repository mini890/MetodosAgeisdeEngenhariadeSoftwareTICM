from django.test import TestCase
from django.urls import resolve
from todo.views import home_page


# Create your tests here.

class FirstTest(TestCase):
    def test_erro_aritmetica(self):
        self.assertEqual(1 + 1, 2)

    def test_url_devolve_homepage(self):
        resultado = resolve("/")
        self.assertEqual(resultado.func, home_page)
