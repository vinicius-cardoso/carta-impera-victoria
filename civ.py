from baralho import Baralho
from jogador import Jogador


ERA_1 = 1
ERA_2 = 2
ERA_3 = 3

NUMERO_MIN_JOGADORES = 2
NUMERO_MAX_JOGADORES = 4

EFEITOS_NIVEL_1 = 3
EFEITOS_NIVEL_2 = 5

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

    def escolher_carta(self, jogador):
        while True:
            try:
                id_carta_a_jogar = int(
                    input('Escolha uma carta da sua mão para jogar: ')
                )
                
                if id_carta_a_jogar in jogador.get_id_de_cartas():
                    return id_carta_a_jogar
                else:
                    print('Essa carta não está em sua mão.')
            except ValueError:
                print('Por favor, insira um valor válido.')

    def usar_efeitos(self):
        while True:
            try:
                escolha = input('Deseja usar efeitos de cartas? (s/n): ')
                
                if escolha == 's':
                    return True
                if escolha == 'n':
                    return False
                else:
                    print('Por favor, insira um valor válido.')
            except ValueError:
                print('Por favor, insira um valor válido.')

    def permanente_ou_sacrificio(self):
        while True:
            try:
                escolha = input(
                    'Efeitos permanentes ou Efeitos de sacrifício? (p/s): '
                )
                
                if escolha == 'p':
                    return 'permanente'
                if escolha == 's':
                    return 'sacrificio'
                else:
                    print('Por favor, insira um valor válido.')
            except ValueError:
                print('Por favor, insira um valor válido.')

    def fase_1(self, jogador):
        id_carta_a_jogar = self.escolher_carta(jogador)
        carta_a_jogar = jogador.get_carta(id_carta_a_jogar)
        
        jogador.baixar_carta(carta_a_jogar)

    def fase_2(self, jogador):
        if self.usar_efeitos():            
            if jogador.pode_usar_efeitos_permanentes(EFEITOS_NIVEL_1):
                tipo_efeito = self.permanente_ou_sacrificio()
                    
                if tipo_efeito == 'permamente':
                    jogador.usar_efeitos_permanentes()
                if tipo_efeito == 'sacrificio':
                    jogador.usar_efeitos_de_sacrificio()
            else:
                jogador.usar_efeitos_de_sacrificio()

    def fase_3(self, jogador):
        while len(jogador.get_mao()) < jogador.limite_de_cartas:
            jogador.comprar_carta(self.baralho.distribuir_carta())

    def iniciar_jogo(self):
        for jogador in self.jogadores:
            print(80 * '-')
            print(f'Cartas na mão de {jogador.get_nome()}:')
            print(80 * '-')

            for carta in jogador.get_mao():
                print(carta)
            
            print(80 * '-')

            # Fase 1. Baixar uma carta (obrigatório)
            self.fase_1(jogador)

            # Fase 2. Usar efeitos de cartas (opcional)
            self.fase_2(jogador)

            # Fase 3. Comprar cartas (obrigatório)
            self.fase_3(jogador)

def definir_numero_de_jogadores():
    while True:
        try:
            numero_de_jogadores = int(input('Número de jogadores (2-4): '))

            if numero_de_jogadores in range(
                NUMERO_MIN_JOGADORES, NUMERO_MAX_JOGADORES + 1
            ):
                return numero_de_jogadores
            else:
                print('O número de jogadores deve ser entre 2 e 4.')
        except ValueError:
            print('Por favor, insira um número válido.')

def main():
    numero_de_jogadores = definir_numero_de_jogadores()

    print(80 * '-')

    civ = CIV(numero_de_jogadores)
    civ.set_jogadores()

    if numero_de_jogadores == 2:
        civ.cartas_para_vencer = 8

    baralho = Baralho()
    baralho.embaralhar()

    if numero_de_jogadores in [2, 3]:
        baralho.remover_3_cartas_de_cada_era()

    baralho.juntar_eras_ordenadas()

    civ.set_baralho(baralho)
    civ.distribuir_mao_inicial()
    civ.iniciar_jogo()

if __name__ == '__main__':
    main()
