# Criando a classe formaGeometrica Classe Pai

class FormaGeometrica:
    def calc_area(self):
        pass

# Criando  a Sub-Classe quadrado, circulo

class Quadrado(FormaGeometrica):
    def __init__(self, base):
        self.base = base

    def calc_area(self):
        return self.base * self.base

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calc_area(self):
        return self.raio * self.raio * 3.14

# Utilizando o Polimorfismo
quad1 = Quadrado(2)
quad2 = Quadrado(3)
circ1 = Circulo(1)
circ2 = Circulo(2)

formas_geometricas = [quad1, quad2, circ1, circ2]

soma = 0    # acumulador
for forma in formas_geometricas:               # forma =  é o contador
    soma = soma + forma.calc_area()

    print(f'A Area foi de {soma}')
