from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewTodoTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_startListOfToDos(self):
        # verificar que existe um site ativo naquele endereço
        self.browser.get("http://localhost:8000")
        # verificar que é o site dos todo's
        self.assertIn('To-Do', self.browser.title)
        # Tenho um interface para escrever o ToDo
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter to do")
        # Escrevo "Alimentar o gato"
        # carrego Enter
        inputbox.send_keys("Alimentar o gato")
        inputbox.send_keys(Keys.ENTER)
        # Aparece no ecrâ
        # "1: Alimentar o gato"
        self.fail("Não implementado")
        # Escrevo "Comprar Leite" seguido de enter
        # Aparece no ecrâ
        # "1: Alimentar o gato"
        # "2: Comprar Leite"
        # ...
