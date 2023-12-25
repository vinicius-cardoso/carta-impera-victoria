efeitos_de_sacrificio = (
    (
        'Ataque', 
        'Sacrifique 1 carta de Poder Militar da sua área de jogo e coloque-a \
        na pilha de descarte.\nEscolha uma Esfera de Poder. Descarte 1 carta \
        em sua área de jogo dessa Esfera de Poder. Cada jogador deverá \
        descartar uma carta em sua área de jogo do mesmo tipo, se possível.'
    ), 
    (
        'Inquisição', 
        'Sacrifique 1 carta de Religião da sua área de jogo e coloque-a na \
        pilha de descarte. \nEscolha um jogador. Pegue todas as cartas da mão \
        dele e junte-as à sua mão. Escolha com quais você quer ficar e \
        devolva a ele o mesmo número de cartas que ele tinha antes.'
    ),
    (
        'Embargo', 
        'Sacrifique 1 carta de Economia da sua área de jogo e coloque-a \
        virada para baixo horizontalmente sobre uma carta de outro jogador \
        (de qualquer Esfera de Poder).\nAquele jogador não poderá baixar \
        nenhuma carta dessa Esfera de Poder no seu turno, coloque a carta de \
        Economia usada na pilha de descarte.'
    ),
    (
        'Descoberta', 
        'Sacrifique 1 carta de Ciência da sua área de jogo e coloque-a na \
        pilha de descarte.\nCompre 5 cartas do baralho e, em seguida, \
        descarte quaisquer 5 cartas de sua mão. Se houver menos de 5 cartas \
        restantes no baralho, compre todas as cartas disponíveis e descarte o \
        mesmo número de cartas de sua mão.'
    ).
    (
        'Democracia', 
        'Sacrifique 1 carta de Utopia da sua área de jogo e coloque-a virada \
        para baixo sobre uma esfera de poder à sua escolha na área de jogo de \
        outro jogador.\nSua carta permanecerá lá até o fim da partida. Para \
        cada carta de Utopia naquela Esfera de Poder, o jogador afetado \
        precisará de 1 carta adicional naquela Esfera de Poder para ganhar o \
        jogo por Hegemonia. Mais de uma carta pode ser colocada em uma mesma \
        Esfera.'
    ),
)

class EfeitoDeSacrifico:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao
