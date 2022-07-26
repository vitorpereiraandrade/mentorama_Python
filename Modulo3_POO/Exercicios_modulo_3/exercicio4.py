class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = idade

    def engordar(self,engordar):
        self.engordar = peso / (altura * altura)
        if self.engordar < 18.5:
            print(f"{nome}, seu IMC {engordar} está baixo, precisa engordar")
        return self.engordar

    def emagrecer(self,emagrecer):
        self.emagrecer = peso / (altura * altura)
        if self.emagrecer > 24.9:
            print(f"{nome}, seu IMC {emagrecer} está alto, precisa emagracer")
        return self.emagrecer

    def crescer(self):
        if idade < 21:
            resultado = 20 - idade
            self.idade = resultado * 0.5

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

resultado = Pessoa(nome, idade, peso, altura)

print(f'{nome}, sua idade é {idade} anos, seu peso é {peso}, e sua altura é {altura}')





