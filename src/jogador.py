from src.carta import Carta
from src.input_valido import input_valido

class Jogador:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.mao = []
        self.area_de_jogo = {
            Carta.PODER_MILITAR: [], 
            Carta.RELIGIAO: [], 
            Carta.ECONOMIA: [], 
            Carta.CIENCIA: [], 
            Carta.ARTES: [], 
            Carta.UTOPIA: []
        }
        self.limite_de_cartas = 3

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_mao(self):
        return self.mao

    def get_area_de_jogo(self):
        return self.area_de_jogo

    def get_carta(self, id):
        return next((carta for carta in self.mao if carta.id == id), None)

    def get_id_de_cartas(self):
        return [carta.get_id() for carta in self.mao]

    def comprar_carta(self, carta):
        self.mao.append(carta)

    def baixar_carta(self, carta):
        for carta_mao in self.mao:
            if carta_mao.get_id() == carta.get_id():
                self.mao.remove(carta_mao)
        
        self.area_de_jogo[carta.get_numero_esfera_de_poder()].append(carta)        

    def pode_usar_efeitos_permanentes(self, efeitos_nivel_1):
        return any(
            len(self.area_de_jogo[esfera_de_poder]) >= efeitos_nivel_1
            for esfera_de_poder in self.area_de_jogo
        )

    def usar_efeitos_permanentes(self):
        print('permanente')

    def mostrar_opcoes(self, opcoes):
        print(80 * '-')
        print(f'Cartas na área de jogo de {self.get_nome()}:')
        print(80 * '-')

        for esfera_de_poder, cartas in self.area_de_jogo.items():
            if cartas:
                ultima_carta = cartas[-1]
                num = ultima_carta.get_numero_esfera_de_poder()
                opcoes.append(num)

                print(
                    f'{num} - '
                    f'{ultima_carta.get_nome_esfera_de_poder()} '
                    f'({len(cartas)})'
                )

    def usar_efeitos_de_sacrificio(self):
        mensagem = 'Qual carta deseja sacrificar? : '
        opcoes = []

        self.mostrar_opcoes(opcoes)

        return input_valido(mensagem, opcoes)

    def is_vencedor(self, cartas_para_vencer):
        return any(
            len(self.area_de_jogo[esfera_de_poder]) >= cartas_para_vencer
            for esfera_de_poder in self.area_de_jogo
        )
