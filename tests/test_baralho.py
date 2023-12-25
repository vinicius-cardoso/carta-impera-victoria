import unittest
from baralho import Baralho, ERA_1, ERA_2, ERA_3

class TestBaralho(unittest.TestCase):

    def setUp(self):
        self.baralho = Baralho()

    def test_inicializacao(self):
        total_cartas = sum([qtd for _, qtd in Baralho.era_1]) + \
                       sum([qtd for _, qtd in Baralho.era_2]) + \
                       sum([qtd for _, qtd in Baralho.era_3])
        total_inicializado = len(self.baralho.cartas_por_era[ERA_1]) + \
                             len(self.baralho.cartas_por_era[ERA_2]) + \
                             len(self.baralho.cartas_por_era[ERA_3])
        self.assertEqual(total_inicializado, total_cartas)

    def test_embaralhar(self):
        copia_era_1 = self.baralho.cartas_por_era[ERA_1].copy()
        self.baralho.embaralhar()
        self.assertNotEqual(copia_era_1, self.baralho.cartas_por_era[ERA_1])

    def test_distribuir_carta(self):
        self.baralho.juntar_eras_ordenadas()
        carta = self.baralho.distribuir_carta()
        self.assertIsNotNone(carta)

    def test_remover_3_cartas_de_cada_era(self):
        self.baralho.remover_3_cartas_de_cada_era()
        for era in [ERA_1, ERA_2, ERA_3]:
            era_inicial = len(Baralho.era_1) - 3
            self.assertEqual(len(self.baralho.cartas_por_era[era]), era_inicial)

    def test_juntar_eras_ordenadas(self):
        self.baralho.juntar_eras_ordenadas()
        total_cartas = sum(
            len(
                self.baralho.cartas_por_era[era]
            ) for era in [ERA_1, ERA_2, ERA_3]
        )
        self.assertEqual(len(self.baralho.cartas), total_cartas)

if __name__ == '__main__':
    unittest.main()
