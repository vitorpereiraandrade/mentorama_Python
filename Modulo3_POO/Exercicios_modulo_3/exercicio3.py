class Retangulo:
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

    def RetornarValorLados(self):
        print(f'O Comprimento é: {self.comprimento:.2f}')
        print(f'A Altura é: {self.altura:.2f}')

    def CalcularArea(self):
        print(f'A Area do Retangulo é: {self.comprimento * self.altura:.2f}')


a = Retangulo(comprimento=float(input('Informe o Comprimento: ')), altura=float(input('Informe Altura: ')))
a.RetornarValorLados()
a.CalcularArea()




    


