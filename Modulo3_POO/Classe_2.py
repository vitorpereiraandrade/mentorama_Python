# DECLARANDO UMA CLASSE
class Pessoa:
    def __init__(self, nome, idade):     #  ---- > CONSTRUTOR
        self.nome = nome
        self.idade = idade

    def setNome(self,nome):             # ---> METODO
        self.nome = nome                # ---> CORPO DO METODO

    def setIdade(self, idade):          # ---> METODO
        self.idade = idade              # ---> CORPO DO METODO

    def getNome(self):                 # FUNCAO QUE RETORNO O NOME
        return self.nome

    def getIdade(self):                # FUNCAO QUE RETORNA A IDADE
        return self.idade