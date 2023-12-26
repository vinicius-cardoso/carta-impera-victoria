from src.baralho import Baralho
from src.jogador import Jogador
from src.input_valido import input_valido, converter_opcoes_em_str


EFEITOS_NIVEL_1 = 3
EFEITOS_NIVEL_2 = 5
SEPARADOR = 80 * '-'
CARTAS_MAO_INICIAL = 3
MIN_JOGADORES = 2
MAX_JOGADORES = 4

class CIV:
    def __init__(self):
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

    def configurar_jogo(self, numero_de_jogadores):
        self.numero_de_jogadores = numero_de_jogadores
        self.set_jogadores()
        self.ajustar_condicao_vitoria()
        self.preparar_baralho()

    def ajustar_condicao_vitoria(self):
        if self.numero_de_jogadores == 2:
            self.cartas_para_vencer = 8

    def preparar_baralho(self):
        baralho = Baralho()
        baralho.embaralhar()

        if self.numero_de_jogadores in {2, 3}:
            baralho.remover_3_cartas_de_cada_era()

        baralho.juntar_eras_ordenadas()
        self.set_baralho(baralho)

    def distribuir_mao_inicial(self):
        for jogador in self.jogadores:
            for _ in range(CARTAS_MAO_INICIAL):
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
        while len(jogador.mao) < jogador.limite_de_cartas:
            jogador.comprar_carta(self.baralho.distribuir_carta())

    def iniciar_jogo(self):
        for jogador in self.jogadores:
            print(SEPARADOR)
            print(f'Cartas na mão de {jogador.nome}:')
            print(SEPARADOR)

            for carta in jogador.mao:
                print(carta)
            
            print(SEPARADOR)

            # Fase 1. Baixar uma carta (obrigatório)
            self.fase_1(jogador)

            # Fase 2. Usar efeitos de cartas (opcional)
            self.fase_2(jogador)

            # Fase 3. Comprar cartas (obrigatório)
            self.fase_3(jogador)

def obter_numero_jogadores():
    mensagem = 'Número de jogadores (2-4): '
    opcoes = converter_opcoes_em_str(range(MIN_JOGADORES, MAX_JOGADORES + 1))

    return int(input_valido(mensagem, opcoes))

def main():
    print(SEPARADOR)
    numero_de_jogadores = obter_numero_jogadores()
    print(SEPARADOR)

    jogo = CIV()
    jogo.configurar_jogo(numero_de_jogadores)
    jogo.distribuir_mao_inicial()
    jogo.iniciar_jogo()

if __name__ == '__main__':
    main()
