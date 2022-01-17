class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def valorLado(self, novo_valor_lado):
        self.tamanho_lado = novo_valor_lado

    def retornaValor(self):
        return self.tamanho_lado

    def areaQuadrado(self):
        return self.tamanho_lado * self.tamanho_lado

quadrado = Quadrado(int(input('Informe o tamanho do lado do quadrado: ')))
print(f'O tamanho dos lados do quadrado é: {quadrado.tamanho_lado}')

quadrado.areaQuadrado()
print(f'O tamanho da area do quadrado é: {quadrado.areaQuadrado()}')







