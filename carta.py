class Carta:
    PODER_MILITAR = 1
    RELIGIAO = 2
    ECONOMIA = 3
    CIENCIA = 4
    ARTES = 5
    UTOPIA = 6

    NUMERO = 0
    NOME = 1
    SIGLA = 2

    def __init__(self, id, esfera_de_poder, era):
        self.id = id
        self.esfera_de_poder = esfera_de_poder
        self.era = era

    def __repr__(self):
        return (
            f'{self.id} - '                
            f'{self.esfera_de_poder[self.NOME]} ' 
            f'({self.esfera_de_poder[self.SIGLA]}) - '
            f'Era {self.era}'
        )

    def get_id(self):
        return self.id

    def get_numero_esfera_de_poder(self):
        return self.esfera_de_poder[self.NUMERO]

    def get_nome_esfera_de_poder(self):
        return self.esfera_de_poder[self.NOME]

    def get_sigla_esfera_de_poder(self):
        return self.esfera_de_poder[self.SIGLA]
