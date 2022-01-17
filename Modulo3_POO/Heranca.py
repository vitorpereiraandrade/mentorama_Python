# DECLARANDO A CLASSE PAI

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimenome(self):
        print(self.nome, self.sobrenome)

# USAMOS A CLASSE PESSOA PARA CRIAR UM OBJETO x, e entao executamos o metódo impressao

x = Pessoa('Jose', 'Silva')
x.imprimenome()

# DECLARANDO A CLASSE FILHA

class Estudante(Pessoa):
    pass

# USAMOS A CLASSE FILHA Estudante PARA CRIAR UM OBJETO y, E ENTAO EXECUTAMOS O METODO IMPRESSAO

y = Estudante('Tiago', 'Silva')
y.imprimenome()