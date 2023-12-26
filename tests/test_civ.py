import unittest
from unittest.mock import patch

from src.civ import CIV
from src.baralho import Baralho
from src.jogador import Jogador

class TestCIV(unittest.TestCase):
    def setUp(self):
        self.jogo = CIV()
    
    @patch('src.civ.input', create=True)
    def test_set_jogadores(self, mock_input):
        mock_input.return_value = 'Alice'
        self.jogo.configurar_jogo(1)
        self.assertEqual(len(self.jogo.jogadores), 1)
        self.assertIsInstance(self.jogo.jogadores[0], Jogador)
        self.assertEqual(self.jogo.jogadores[0].nome, 'Alice')

    def test_configurar_jogo(self):
        with patch.object(CIV, 'set_jogadores') as mock_set_jogadores, \
             patch.object(CIV, 'ajustar_condicao_vitoria') as mock_ajustar_condicao, \
             patch.object(CIV, 'preparar_baralho') as mock_preparar_baralho:
            self.jogo.configurar_jogo(3)
            mock_set_jogadores.assert_called_once()
            mock_ajustar_condicao.assert_called_once()
            mock_preparar_baralho.assert_called_once()

    @patch('src.civ.input', create=True)
    def test_ajustar_condicao_vitoria(self, mock_input):
        mock_input.return_value = 'Alice'
        self.jogo.configurar_jogo(2)
        self.assertEqual(self.jogo.cartas_para_vencer, 8)

    @patch('src.civ.input', create=True)
    def test_preparar_baralho(self, mock_input):
        mock_input.return_value = 'Alice'
        self.jogo.configurar_jogo(3)
        self.jogo.preparar_baralho()

        self.assertIsInstance(self.jogo.baralho, Baralho)

if __name__ == '__main__':
    unittest.main()
