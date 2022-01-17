# Class
# Syntaxe

# Marca, Memoria Ram, Placa de Video (propriedades) - (atributos)
# _init_  - Chamado de construtor e podera criar as funcoes inicias do seu computador
# SELF  - serve pra vc acessar as propriedades ou
# metodos de uma instancia

class Computador:
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video

# METODOS - Ligar, Desligar, Exibir Configuracoes
    def Ligar(self):
        print('Estou ligado')        # aqui todos os comandos que o metodo Ligar for fazer

    def Desligar(self):
        print('Estou desligando')

    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_video)

#Agora vamos criar um instancia da classe

computador1 = Computador('Asus', '16gb', 'nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()
