class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print('O carro ligou')

    def desligar(self):
        print('O carro desligou')

    def imprimir(self):
        print(f'O carro possui a cor: {self.cor} ')
        print(f'O carro é da marca: {self.marca}')
        print(f'o Carro é do modelo: {self.modelo}')

carro1 = Carro('azul','Gm', 'Cruze')
carro2 = Carro('preto', 'Honda', 'Civic')

carro1.ligar()
carro1.desligar()
carro1.imprimir()

carro2.ligar()
carro2.desligar()
carro2.imprimir()