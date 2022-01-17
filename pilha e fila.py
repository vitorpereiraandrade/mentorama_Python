# Criando e manipulando pilhas (lifo)
pilha = [3, 1, 5]
print(pilha)
pilha.append(2)
print(pilha)
pilha.pop()
print(pilha)
pilha.pop()
print(pilha)
pilha.pop()
print(pilha)

# Criando e manipulando filas (fifo)

from collections import deque
fila = deque([5, 8])
print(fila)
fila.append(10)
print(fila)
fila.popleft()
print(fila)
