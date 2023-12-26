efeitos_permanentes_nivel_1 = (
    (
        'Assassinato', 
        'Descarte 1 carta de sua mão.'
    ), 
    (
        'Escritura Sagrada', 
        'Aumente o limite de sua mão em 2. Agora seu limite é de 5 cartas.'
    ),
    (
        'Desenvolvimento', 
        'Descarte 1 carta qualquer de sua área de jogo e imediatamente baixe \
        1 carta qualquer de sua mão.'
    ),
    (
        'Experimento', 
        'Retorne à sua mão 1 carta de sua área de jogo. Em seguida, baixe 1 \
        carta de sua mão.'
    ).
    (
        'Oligarquia', 
        'Escolha 1 carta da pilha de descarte e coloque-a em sua mão.'
    ),
)

efeitos_permanentes_nivel_2 = (
    (
        'Expiação', 
        'Descarte 2 cartas de sua mão.'
    ), 
    (
        'Direito Divino', 
        'Aumente o limite de sua mão em 4. Agora seu limite é de 7 cartas.'
    ),
    (
        'Monopólio', 
        'Descarte 2 carta quaisquer de sua área de jogo e imediatamente baixe \
        2 cartas quaisquer de sua mão.'
    ),
    (
        'Pesquisa', 
        'Retorne à sua mão 2 cartas de sua área de jogo. Em seguida, baixe 2 \
        cartas de sua mão.'
    ).
    (
        'República', 
        'Escolha 2 cartas da pilha de descarte e coloque-as em sua mão.'
    ), 
)

efeito_artes = (
    'Inspiração', 
    'Copie 1 efeito permanente (nível 1 ou nível 2) a que outro jogador \
    tenha acesso.'
)

class EfeitoPermanente:
    def __init__(self, nome, descricao, nivel):
        self._nome = nome
        self._descricao = descricao
        self._nivel = nivel

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def nivel(self):
        return self._nivel
