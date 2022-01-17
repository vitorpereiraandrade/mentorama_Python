# CLASSES, OBJETOS E METODOS
# Como primeiro exemplo, vamos modelar uma classe Televisao com seus respectivos metodos e atributos de maneira simples.

# DECLARANDO UMA CLASSE

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2


tv = Televisao()  # CRIAMOS UM OBJETO TV QUE RECEBE A CLASSE TELEVISAO
print(tv.ligada)  # EXIBIMOS O VALOR ATRIBUTO LIGADA AO OBJETO TV
print(tv.canal)   # EXIBIMOS O VALOR ATRIBUIDO LIGADA DO OBJETO TV
print(tv.sala)    # VAI DAR ERRO, NAO FOI DECLARADA  - NAO EXISTE SALA




