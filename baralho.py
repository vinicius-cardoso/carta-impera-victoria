import random

from carta import Carta


ERA_1 = 1
ERA_2 = 2
ERA_3 = 3

class Baralho:
    era_1 = (
        ((Carta.PODER_MILITAR, 'Poder Militar', 'P'), 8),
        ((Carta.RELIGIAO, 'Religião', 'R'), 8),
        ((Carta.ECONOMIA, 'Economia', 'E'), 4),
        ((Carta.CIENCIA, 'Ciência', 'C'), 4),
        ((Carta.ARTES, 'Artes', 'A'), 4),
        ((Carta.UTOPIA, 'Utopia', 'U'), 0),
    )

    era_2 = (
        ((Carta.PODER_MILITAR, 'Poder Militar', 'P'), 8),
        ((Carta.RELIGIAO, 'Religião', 'R'), 8),
        ((Carta.ECONOMIA, 'Economia', 'E'), 4),
        ((Carta.CIENCIA, 'Ciência', 'C'), 8),
        ((Carta.ARTES, 'Artes', 'A'), 4),
        ((Carta.UTOPIA, 'Utopia', 'U'), 0),
    )

    era_3 = (
        ((Carta.PODER_MILITAR, 'Poder Militar', 'P'), 4),
        ((Carta.RELIGIAO, 'Religião', 'R'), 0),
        ((Carta.ECONOMIA, 'Economia', 'E'), 8),
        ((Carta.CIENCIA, 'Ciência', 'C'), 8),
        ((Carta.ARTES, 'Artes', 'A'), 8),
        ((Carta.UTOPIA, 'Utopia', 'U'), 16),
    )

    cartas_era_1 = []
    cartas_era_2 = []
    cartas_era_3 = []

    def __init__(self):
        id = 1

        for esfera_de_poder, qtd in self.era_1:
            for _ in range(qtd):
                self.cartas_era_1.append(
                    Carta(id, esfera_de_poder, ERA_1)
                )
                id += 1

        for esfera_de_poder, qtd in self.era_2:
            for _ in range(qtd):
                self.cartas_era_2.append(
                    Carta(id, esfera_de_poder, ERA_2)
                )
                id += 1

        for esfera_de_poder, qtd in self.era_3:
            for _ in range(qtd):
                self.cartas_era_3.append(
                    Carta(id, esfera_de_poder, ERA_3)
                )
                id += 1

        self.cartas_por_era = {
            ERA_1: self.cartas_era_1, 
            ERA_2: self.cartas_era_2, 
            ERA_3: self.cartas_era_3
        }

        self.cartas = []

    def __len__(self):
        return sum(len(cartas) for cartas in self.cartas.values())

    def embaralhar(self):
        for era in self.cartas_por_era:
            random.shuffle(self.cartas_por_era[era])

    def distribuir_carta(self):
        return self.cartas.pop() if self.cartas else None

    def remover_3_cartas_de_cada_era(self):
        for era in self.cartas_por_era:
            for _ in range(3):            
                self.cartas_por_era[era].pop()

    def juntar_eras_ordenadas(self):
        self.cartas = self.cartas_por_era[ERA_3] + \
                      self.cartas_por_era[ERA_2] + \
                      self.cartas_por_era[ERA_1]

