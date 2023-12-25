MSG_VALOR_VALIDO = 'Por favor, insira um valor válido.'

def input_valido(mensagem, opcoes):
    while True:
        try:
            escolha = input(mensagem)

            if escolha in opcoes:
                return escolha
            else:
                print(MSG_VALOR_VALIDO)
        except ValueError:
            print(MSG_VALOR_VALIDO)

def converter_opcoes_em_str(opcoes):
    return [str(numero) for numero in opcoes]
