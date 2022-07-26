class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_valor_dos_lados(self, novo_comprimento, novo_largura):
        self.comprimento = novo_comprimento
        self.largura = novo_largura

    def retornar_valor_dos_lados(self, valor):
        return valor

    def calcular_area(self):
        area = self.largura * self.comprimento
        return area

    def calcular_perimetro(self):
        perimetro = (2 * self.largura) + (2 * self.comprimento)
        return perimetro

largura = float(input("Informe a largura: "))
comprimento = float(input("Informe a comprimento: "))

local = Retangulo(largura, comprimento)

print(f'Serão necessários {local.calcular_area():.2f} metros quadrados de piso')
print(f'Serão necessarios {local.calcular_perimetro():.2f} metros de rodapé')















    


