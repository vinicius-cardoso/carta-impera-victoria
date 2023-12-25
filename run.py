import unittest
import sys

# Importe os testes dos módulos carta e baralho
from tests.test_carta import TestCarta
from tests.test_baralho import TestBaralho
from civ import main

def main():
    print("Testes passaram, executando o programa principal...")
    main()

if __name__ == '__main__':
    # Carrega os testes dos módulos
    suite_carta = unittest.TestLoader().loadTestsFromTestCase(TestCarta)
    suite_baralho = unittest.TestLoader().loadTestsFromTestCase(TestBaralho)

    # Combinar todas as suites de teste em uma grande suite
    all_tests = unittest.TestSuite([suite_carta, suite_baralho])

    # Executar os testes
    result = unittest.TextTestRunner().run(all_tests)

    if result.wasSuccessful():
        main()
    else:
        sys.exit("Testes falharam, abortando a execução.")
