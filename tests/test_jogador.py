import unittest
from unittest.mock import patch
from src.jogador import Jogador
from src.carta import Carta

class TestJogador(unittest.TestCase):
    def setUp(self):
        self.jogador = Jogador(1, 'Alice')

    def test_init(self):
        self.assertEqual(self.jogador.id, 1)
        self.assertEqual(self.jogador.nome, 'Alice')
        self.assertEqual(len(self.jogador.mao), 0)
        self.assertEqual(len(self.jogador.area_de_jogo[Carta.PODER_MILITAR]), 0)

    def test_get_carta(self):
        carta = Carta(1, (Carta.PODER_MILITAR, 'Poder Militar', 'P'), 1)
        self.jogador.comprar_carta(carta)
        self.assertIsNotNone(self.jogador.get_carta(1))

    def test_comprar_carta(self):
        carta = Carta(2, (Carta.RELIGIAO, 'Religião', 'R'), 1)
        self.jogador.comprar_carta(carta)
        self.assertEqual(len(self.jogador.mao), 1)

    def test_baixar_carta(self):
        carta = Carta(3, (Carta.ECONOMIA, 'Economia', 'E'), 1)
        self.jogador.comprar_carta(carta)
        self.jogador.baixar_carta(carta)
        self.assertEqual(len(self.jogador.mao), 0)
        self.assertEqual(len(self.jogador.area_de_jogo[Carta.ECONOMIA]), 1)

    def test_pode_usar_efeitos_permanentes(self):
        carta = Carta(4, (Carta.CIENCIA, 'Ciência', 'C'), 1)
        self.jogador.comprar_carta(carta)
        self.jogador.baixar_carta(carta)
        self.assertFalse(self.jogador.pode_usar_efeitos_permanentes(3))

    def test_is_vencedor(self):
        self.assertFalse(self.jogador.is_vencedor(7))

if __name__ == '__main__':
    unittest.main()
