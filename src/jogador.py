from src.carta import Carta
from src.input_valido import input_valido

class Jogador:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self._mao = []
        self._area_de_jogo = {
            Carta.PODER_MILITAR: [], 
            Carta.RELIGIAO: [], 
            Carta.ECONOMIA: [], 
            Carta.CIENCIA: [], 
            Carta.ARTES: [], 
            Carta.UTOPIA: []
        }
        self.limite_de_cartas = 3

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def mao(self):
        return self._mao

    @property
    def area_de_jogo(self):
        return self._area_de_jogo

    def get_carta(self, id):
        return next((carta for carta in self.mao if carta.id == id), None)

    def get_id_de_cartas(self):
        return [carta.id for carta in self.mao]

    def comprar_carta(self, carta):
        if len(self.mao) < self.limite_de_cartas:
            self.mao.append(carta)

    def baixar_carta(self, carta):
        if carta in self.mao:
            self.mao.remove(carta)
            self.area_de_jogo[
                carta.esfera_de_poder[Carta.NUMERO]
            ].append(carta)

    def pode_usar_efeitos_permanentes(self, efeitos_nivel_1):
        return any(
            len(self.area_de_jogo[esfera_de_poder]) >= efeitos_nivel_1
            for esfera_de_poder in self.area_de_jogo
        )

    def usar_efeitos_permanentes(self):
        print('permanente')

    def mostrar_opcoes(self, opcoes):
        print(80 * '-')
        print(f'Cartas na área de jogo de {self.nome}:')
        print(80 * '-')

        for esfera_de_poder, cartas in self.area_de_jogo.items():
            if cartas:
                ultima_carta = cartas[-1]
                num = ultima_carta.esfera_de_poder[Carta.NUMERO]

                opcoes.append(num)

                print(f'{num} - {ultima_carta.esfera_de_poder[Carta.NOME]} '
                      f'({len(cartas)})'
                )

    def usar_efeitos_de_sacrificio(self):
        mensagem = 'Qual carta deseja sacrificar? : '
        opcoes = []

        self.mostrar_opcoes(opcoes)

        return input_valido(mensagem, opcoes)

    def is_vencedor(self, cartas_para_vencer):
        return any(
            len(cartas) >= cartas_para_vencer 
            for cartas in self.area_de_jogo.values()
        )
