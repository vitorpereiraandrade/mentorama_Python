import threading
import time
from threading import Thread

# INICIALIZANDO UM THREAD COM CLASSES

class MinhaThread:
    def mostraNumeros(self):
        i = 0
        print(threading.current_thread().getName())
        time.sleep(1)
        while(i<=10):
            print(i)
            i+=1
obj = MinhaThread()
t5 = Thread(target=obj.mostraNumeros())
t5.start()

t6 = Thread(target=obj.mostraNumeros())
t6.start()

t7 = Thread(target=obj.mostraNumeros())
t7.start()

##### Aplicando o conceito de threads #####

"""Vamos considerar o diagrama abaixo, no qual um processo contém dois threads ativos:
* O código abaixo ilustra a utilização de threads em um programa que imprime o quadrado e o cubo de um determinado número
* As entradas são definidas por um mesmo valor inteiro, armazenado na variável num """


def print_cube(num):
    """
    function para imprimir o cubo de um determinado num
    """
    time.sleep(5)
    print(f'Cube: {num*num*num}')


def print_square(num):
    """
    função para imprimir o quadrado de um determinado num
    """
    time.sleep(10)
    print(f'Square: {num * num}')


if __name__ == "__main__":
    # criando threads
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # iniciando o thread 1
    t1.start()
    # iniciando o thread 2
    t2.start()

    # aguarde até o thread 1 seja executado completamente
    t1.join()
    # aguarde até o thread 2 seja executado completamente
    t2.join()

    # ambos os threads foram completamente executados
    print("Done!")

