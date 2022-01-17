# modulo soma (que importa Modulo_entrada_script)

import Modulo_entrada_script
lista = []
for x in range(10):
    lista.append(Modulo_entrada_script.valida_inteiro('Digite um numero:', 0, 20))
print(f'Soma: {sum(lista)}')