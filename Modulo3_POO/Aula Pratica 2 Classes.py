# VAMOS ATRIBUIR NOVOS METODOS A CLASSE TELEVISAO

class Televisao:
    def __init__(self, ligada, canal):
        self.ligada = ligada
        self.canal = canal

    def ligar(self):
        print('A TV esta ligada')
    def desligar(self):
        print('A TV esta desligada')
    def status_canal(self, canal):
        print(f'O canal é {canal}')

# VAMOS CRIAR INSTANCIAS DA CLASSE

tv1 = Televisao('True', '2')
tv2 = Televisao('False', '5')
print(tv1.canal)          # Isso é só pra ver os parametros que esta acontecendo, para ter uma nocao, imprime individualmente
print(tv1.ligada)

tv1.ligar()
tv1.desligar()
tv1.status_canal(5)