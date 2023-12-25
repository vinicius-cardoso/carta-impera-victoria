from src.baralho import Baralho
from src.jogador import Jogador
from src.input_valido import input_valido, converter_opcoes_em_str


EFEITOS_NIVEL_1 = 3
EFEITOS_NIVEL_2 = 5
SEPARADOR = 80 * '-'
MIN_JOGADORES = 2
MAX_JOGADORES = 4

class CIV:
    def __init__(self, numero_de_jogadores):
        self.numero_de_jogadores = numero_de_jogadores
        self.jogadores = []
        self.baralho = []
        self.pilha_de_descarte = []
        self.cartas_para_vencer = 7

    def set_jogadores(self):
        for id in range(1, self.numero_de_jogadores + 1):
            nome_jogador = input(f'Nome do jogador {id}: ')

            self.jogadores.append(Jogador(id, nome_jogador))

    def set_baralho(self, baralho):
        self.baralho = baralho

    def distribuir_mao_inicial(self):
        for jogador in self.jogadores:
            for _ in range(3):
                jogador.comprar_carta(self.baralho.distribuir_carta())

    def fase_1(self, jogador):
        mensagem = 'Escolha uma carta da sua mão para jogar: '
        opcoes = converter_opcoes_em_str(jogador.get_id_de_cartas())

        id_carta_a_jogar = int(input_valido(mensagem, opcoes))
        carta_a_jogar = jogador.get_carta(id_carta_a_jogar)

        jogador.baixar_carta(carta_a_jogar)

    def fase_2(self, jogador):
        mensagem = 'Deseja usar efeitos de cartas? (s/n): '
        opcoes = ['s', 'n']

        if input_valido(mensagem, opcoes) == 's':
            if jogador.pode_usar_efeitos_permanentes(EFEITOS_NIVEL_1):
                mensagem = 'Efeitos permanentes ou de sacrifício? (p/s): '
                opcoes = ['p', 's']

                tipo_efeito = input_valido(mensagem, opcoes)

                if tipo_efeito == 'p':
                    jogador.usar_efeitos_permanentes()
                if tipo_efeito == 's':
                    jogador.usar_efeitos_de_sacrificio()
            else:
                jogador.usar_efeitos_de_sacrificio()

    def fase_3(self, jogador):
        while len(jogador.get_mao()) < jogador.limite_de_cartas:
            jogador.comprar_carta(self.baralho.distribuir_carta())

    def iniciar_jogo(self):
        for jogador in self.jogadores:
            print(SEPARADOR)
            print(f'Cartas na mão de {jogador.get_nome()}:')
            print(SEPARADOR)

            for carta in jogador.get_mao():
                print(carta)
            
            print(SEPARADOR)

            # Fase 1. Baixar uma carta (obrigatório)
            self.fase_1(jogador)

            # Fase 2. Usar efeitos de cartas (opcional)
            self.fase_2(jogador)

            # Fase 3. Comprar cartas (obrigatório)
            self.fase_3(jogador)

def main():
    mensagem = 'Número de jogadores (2-4): '
    opcoes = converter_opcoes_em_str(range(MIN_JOGADORES, MAX_JOGADORES + 1))

    numero_de_jogadores = int(input_valido(mensagem, opcoes))

    print(SEPARADOR)

    civ = CIV(numero_de_jogadores)
    civ.set_jogadores()

    if numero_de_jogadores == 2:
        civ.cartas_para_vencer = 8

    baralho = Baralho()
    baralho.embaralhar()

    if numero_de_jogadores in {2, 3}:
        baralho.remover_3_cartas_de_cada_era()

    baralho.juntar_eras_ordenadas()

    civ.set_baralho(baralho)
    civ.distribuir_mao_inicial()
    civ.iniciar_jogo()

if __name__ == '__main__':
    main()
