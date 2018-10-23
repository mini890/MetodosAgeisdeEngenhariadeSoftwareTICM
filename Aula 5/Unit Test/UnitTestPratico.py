import unittest
import testPraticoProgram


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.nome = "Carlos JOsÉ mAnUEL"
        self.nome2 = "Carlos     JOsÉ mAnUEL     "
        self.nome3 = "Carlos     JOsÉ de mAnUEL"

    def test_isCorrigido1(self):
        self.assertEqual("Carlos José Manuel", testPraticoProgram.corrigirNome(self.nome))

    def test_isCorrigido2(self):
        self.assertEqual("Carlos José Manuel", testPraticoProgram.corrigirNome(self.nome2))

    def test_isCorrigido3(self):
        self.assertEqual("Carlos José de Manuel", testPraticoProgram.corrigirNome(self.nome3))


if __name__ == '__main__':
    unittest.main()
