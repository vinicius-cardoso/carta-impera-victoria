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
        self._id = id
        self._esfera_de_poder = esfera_de_poder
        self._era = era

    def __repr__(self):
        return (
            f'{self.id} - '                
            f'{self._esfera_de_poder[self.NOME]} ' 
            f'({self._esfera_de_poder[self.SIGLA]}) - '
            f'Era {self.era}'
        )

    @property
    def id(self):
        return self._id

    @property
    def era(self):
        return self._era

    @property
    def esfera_de_poder(self):
        return self._esfera_de_poder
