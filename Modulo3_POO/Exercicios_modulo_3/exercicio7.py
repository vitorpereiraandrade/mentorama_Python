class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume


    def alterar_canal(self, botao):
        if botao > 0 and botao <= 20:
            print(f'Está no canal {botao}')
        else:
            print('Canal Invalido, digite canal de 1 a 20')

    def aumentar_volume(self, botao):
        if botao > 0 and botao <= 20:
            print(f'Esta no volume {botao}')
        elif botao > 20:
            print('Já está no volume máximo')

    def diminuir_volume(self, botao):
        if botao == 0:
            print('Já está no volume minimo')

tv = Tv(1, 15)
tv.alterar_canal(int(input('Digite um canal de 1 a 20: ')))
tv.aumentar_volume(int(input('Digite um volume para aumentar o volume: ')))
tv.diminuir_volume(int(input('Digite para diminuir o volume: ')))















