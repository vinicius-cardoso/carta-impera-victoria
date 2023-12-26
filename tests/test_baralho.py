import unittest
from src.baralho import Baralho, ERA_1, ERA_2, ERA_3

class TestBaralho(unittest.TestCase):
    def setUp(self):
        self.baralho = Baralho()

    def test_init(self):
        baralho = Baralho()
        
        # Verifica se as listas de cartas de cada era foram criadas
        self.assertIsInstance(baralho.cartas_era_1, list)
        self.assertIsInstance(baralho.cartas_era_2, list)
        self.assertIsInstance(baralho.cartas_era_3, list)

        # Verifica se a função inicializar_cartas foi chamada corretamente
        total_era_1 = sum(qtd for _, qtd in baralho.era_1)
        total_era_2 = sum(qtd for _, qtd in baralho.era_2)
        total_era_3 = sum(qtd for _, qtd in baralho.era_3)
        
        self.assertEqual(len(baralho.cartas_era_1), total_era_1)
        self.assertEqual(len(baralho.cartas_era_2), total_era_2)
        self.assertEqual(len(baralho.cartas_era_3), total_era_3)

        # Verifica se o dicionário cartas_por_era foi criado corretamente
        self.assertEqual(baralho.cartas_por_era[ERA_1], baralho.cartas_era_1)
        self.assertEqual(baralho.cartas_por_era[ERA_2], baralho.cartas_era_2)
        self.assertEqual(baralho.cartas_por_era[ERA_3], baralho.cartas_era_3)

        # Verifica se a lista geral de cartas está vazia
        self.assertEqual(len(baralho.cartas), 0)

    def test_inicializar_cartas(self):
        total_cartas = (
            sum(qtd for _, qtd in Baralho.era_1) + \
            sum(qtd for _, qtd in Baralho.era_2) + \
            sum(qtd for _, qtd in Baralho.era_3)
        )
        total_inicializado = (
            len(self.baralho.cartas_por_era[ERA_1]) + \
            len(self.baralho.cartas_por_era[ERA_2]) + \
            len(self.baralho.cartas_por_era[ERA_3])
        )
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
        # Cria uma cópia da lista
        cartas_por_era_antes = {
            ERA_1: self.baralho.cartas_por_era[ERA_1][:], 
            ERA_2: self.baralho.cartas_por_era[ERA_2][:], 
            ERA_3: self.baralho.cartas_por_era[ERA_3][:]
        }

        self.baralho.remover_3_cartas_de_cada_era()

        for era in [ERA_1, ERA_2, ERA_3]:
            expected_len = max(0, len(cartas_por_era_antes[era]) - 3)
            self.assertEqual(
                len(self.baralho.cartas_por_era[era]), expected_len
            )

    def test_juntar_eras_ordenadas(self):
        self.baralho.juntar_eras_ordenadas()
        total_cartas = sum(
            len(
                self.baralho.cartas_por_era[era]
            ) for era in [ERA_1, ERA_2, ERA_3]
        )
        self.assertEqual(len(self.baralho.cartas), total_cartas)

    def test_distribuir_carta_reduz_numero_de_cartas(self):
        self.baralho.juntar_eras_ordenadas()
        total_cartas_inicial = len(self.baralho.cartas)
        self.baralho.distribuir_carta()
        self.assertEqual(len(self.baralho.cartas), total_cartas_inicial - 1)

    def test_remover_3_cartas_com_menos_de_3_cartas(self):
        self.baralho.cartas_por_era[ERA_1] = [1, 2]  # Exemplo com apenas 2 cartas
        self.baralho.remover_3_cartas_de_cada_era()
        self.assertEqual(len(self.baralho.cartas_por_era[ERA_1]), 0)

    def test_len_baralho(self):
        self.baralho.juntar_eras_ordenadas()
        total_cartas = sum(len(
            self.baralho.cartas_por_era[era]
        ) for era in [ERA_1, ERA_2, ERA_3])
        self.assertEqual(len(self.baralho), total_cartas)

if __name__ == '__main__':
    unittest.main()
