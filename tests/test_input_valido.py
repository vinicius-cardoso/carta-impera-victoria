import unittest
from unittest.mock import patch
from src.input_valido import input_valido, converter_opcoes_em_str, \
    MSG_VALOR_VALIDO

class TestInputValido(unittest.TestCase):
    def test_converter_opcoes_em_str(self):
        opcoes = [1, 2, 3]
        resultado_esperado = ['1', '2', '3']
        self.assertEqual(converter_opcoes_em_str(opcoes), resultado_esperado)

    @patch('builtins.input', side_effect=['4', '1'])
    def test_input_valido(self, mock_input):
        opcoes = ['1', '2', '3']
        # O primeiro input ('4') não é válido,
        # então a função deve pedir novamente e aceitar '1'
        resultado = input_valido("Escolha uma opção: ", opcoes)
        self.assertEqual(resultado, '1')

    @patch('builtins.input', side_effect=['a', ValueError(MSG_VALOR_VALIDO), '2'])
    def test_input_valido_com_erro(self, mock_input):
        opcoes = ['1', '2', '3']
        # O primeiro input ('a') gera um ValueError, 
        # então a função deve pedir novamente e aceitar '2'
        resultado = input_valido("Escolha uma opção: ", opcoes)
        self.assertEqual(resultado, '2')

if __name__ == '__main__':
    unittest.main()
