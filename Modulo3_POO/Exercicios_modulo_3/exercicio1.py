class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

bola = Bola('verde', 10, 'couro')
print(f'A cor atual da bola é : {bola.cor}')
print(f'A circuferencia da bola é: {bola.circunferencia}')
print(f"O material da bola é: {bola.material}\n")

bola.trocaCor('amarelo')
print(f'A nova cor da bola é : {bola.mostraCor()}')
