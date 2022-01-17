class Pessoa:                           # Para definir o nome classe usamos a palavra reservada 'class'.
    def __init__(self, nome, idade):    # Para criar um METODO usamos a palavra reservada 'def'
                                        # O CONSTRUTOR é um METODO reservado chamado '_init_'
                                        # O parametro 'self' é obrigatorio e os demais sao definidos por nos
        self.nome = nome                # Aqui esta o corpo do Metodo, sempre identado como manda a sintaxe da linguagem
        self.idade = idade

# A PARTIR DAI PODEMOS DEFINIR QUANTOS METODOS PRECISARMOS

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

