# Inicializa uma lista vazia

lista = list()
print(lista)

# Criando uma lista e consultando os elementos

lista = [3, 2, 10, 1, 0]
print(len(lista))
print(lista[0])
print(lista[0:2])
print(lista[:3])
print(lista[3:])
print(lista[:-1]) # todos os itens menos o ultimo
print(lista[1:-1])
print(lista[:])

# Adicionar elementos em uma lista
lista = ['a']
print(lista)
lista.append('b') # acrescenta
print(lista)
lista.append('c')
print(lista)

# Prolonga uma lista adicianando todos os elementos do argumento passado como parametro
lista.extend('a' 'b' 'c')
print(lista)

# Removendo um elemento da Lista
del lista[1]
print(lista)

# Inserir elementos em uma lista em uma dada posição
lista.insert(0, 'a')
print(lista)

# Remover elementos
lista.remove('a') # vai remover o primeiro elemento 'a'
print(lista)

# Remove um item em uma dada posicao na Lista e retorna.
print(lista.pop(0))
print(lista)


# Contando a quantidade de palavras 'apple' em fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))


