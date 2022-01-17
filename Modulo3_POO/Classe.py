# Declarando uma classe

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa('Maria', '33') # CRIA UM OBJETO PESSOA 1
pessoa2 = Pessoa('Jose', '25') # CRIA UM OBJTETO PESSOA 2
print(pessoa1.nome)  # IMPRIME O VALOR DO NOME
print(pessoa2.nome)  # IMPRIME O VALOR DO NOME
print(pessoa1.idade)