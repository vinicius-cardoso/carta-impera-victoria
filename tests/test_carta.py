import unittest

from src.carta import Carta

class TestCarta(unittest.TestCase):
    def setUp(self):
        esfera_de_poder = (1, 'Poder Militar', 'PM')
        self.carta = Carta(1, esfera_de_poder, 1)

    def test_init(self):
        self.assertEqual(self.carta.id, 1)
        self.assertEqual(self.carta.esfera_de_poder, (1, 'Poder Militar', 'PM'))
        self.assertEqual(self.carta.era, 1)

    def test_repr(self):
        self.assertEqual(repr(self.carta), '1 - Poder Militar (PM) - Era 1')

    def test_get_id(self):
        self.assertEqual(self.carta.id, 1)

    def test_get_numero_esfera_de_poder(self):
        self.assertEqual(self.carta.esfera_de_poder[Carta.NUMERO], 1)

    def test_get_nome_esfera_de_poder(self):
        self.assertEqual(
            self.carta.esfera_de_poder[Carta.NOME], 'Poder Militar'
        )

    def test_get_sigla_esfera_de_poder(self):
        self.assertEqual(self.carta.esfera_de_poder[Carta.SIGLA], 'PM')

if __name__ == '__main__':
    unittest.main()
