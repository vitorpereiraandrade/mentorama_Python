import threading
import time
from threading import Thread

# inicializando um thread com funcao
def func1():
    #faz algo
    for x in range(1,11):
        print(f'Processo 1  - Tarefa {x}')
        x += 1

def func2():
    # faz algo
    for x in range(1,11):
        print(f'Processo 2 - Tarefa {x}')
        x += 1

t1 = Thread(target=func1).start()
t2 = Thread(target=func2).start()

# inicializando um thread com fucnoes e usando o modulo time

def func3():
    #faz algo
    for x in range(1,11):
        print(f'Processo 3  - Tarefa {x}')
        time.sleep(2)
        x += 1

def func4():
    # faz algo
    for x in range(1,11):
        print(f'Processo 4 - Tarefa {x}')
        time.sleep(1)
        x += 1

t3 = Thread(target=func3).start()
t4 = Thread(target=func4).start()

# indentificando o nome do thread atual
print(f'Nome da Thread {threading.currentThread()}')

# indica a quantidade de threads ativas
print(f'Quantidade de Thread {threading.active_count()}')

# mostra uma lista com todos os threads autualmente ativos - lista dos threads
print(f'Lista de Thread {threading.enumerate()}')

# numero que identifica uma thread
print(f'Numero da Thread {threading.get_ident()}')


