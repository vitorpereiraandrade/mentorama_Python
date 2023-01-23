import time
import threading

def proc1():
    time.sleep(5)
    print('Processo1')


def proc2():
    time.sleep(30)
    print('Processo2')

t1 = threading.Thread(target=proc1)
t2 = threading.Thread(target=proc2)
print(f'Objeto criado T1 ativo: {t1.is_alive()}')
print(f'Objeto criado T2 ativo: {t1.is_alive()}')
t1.start()
t2.start()
print('')
print(f'Objeto criado T1 ativo: {t1.is_alive()}')
print(f'Objeto criado T2 ativo: {t1.is_alive()}')






