import threading
def proc1():
    print('Processo 1')

t1 = threading.Thread(target=proc1)
t1.start()
print('')
print(f'Objeto criado Ativo: {t1.is_alive()}')
print(f'Nome thread: {threading.currentThread()}')
print(f'Indentificador: {threading.get_ident()}')
print(f'Quantidade: {threading.active_count()}')
print(f'Lista: {threading.enumerate()}')