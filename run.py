import unittest
import sys

import src.civ as civ
from tests.test_input_valido import TestInputValido
from tests.test_carta import TestCarta
from tests.test_baralho import TestBaralho
from tests.test_jogador import TestJogador
from tests.test_civ import TestCIV

def main():
    print(civ.SEPARADOR)
    civ.main()

if __name__ == '__main__':
    # Carrega os testes dos módulos
    suite_input_valido = unittest.TestLoader().loadTestsFromTestCase(TestInputValido)
    suite_carta = unittest.TestLoader().loadTestsFromTestCase(TestCarta)
    suite_baralho = unittest.TestLoader().loadTestsFromTestCase(TestBaralho)
    suite_jogador = unittest.TestLoader().loadTestsFromTestCase(TestJogador)
    suite_civ = unittest.TestLoader().loadTestsFromTestCase(TestCIV)

    # Combinar todas as suites de teste em uma grande suite
    all_tests = unittest.TestSuite([
        suite_input_valido, 
        suite_carta, 
        suite_baralho, 
        suite_jogador, 
        suite_civ
    ])

    # Executar os testes
    result = unittest.TextTestRunner().run(all_tests)

    if result.wasSuccessful():
        main()
    else:
        sys.exit("Testes falharam, abortando a execução.")
