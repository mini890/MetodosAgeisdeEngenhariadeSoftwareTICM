from django.test import TestCase


# Create your tests here.

class FirstTest(TestCase):
    def test_erro_aritmetica(self):
        self.assertEqual(1 + 1, 2)