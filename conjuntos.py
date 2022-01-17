# Declaracao de um conjunto
meu_set = {1, 2, 3, 4, 1}
print('Conjunto 1', meu_set)
print(type(meu_set))

meu_set2 = set([1, 2, 8, 9, 10])
print('Conjunto 2', meu_set2)
print(type(meu_set2))

# Adicionando elementos
meu_set.add(5)
print('Adicao', meu_set)       # mesma coisa print(f'Adicao {meu_set}')

# Atualizando elemento
meu_set.update([3, 4, 5, 6])
print('Atualizacao', meu_set)

# Removendo elemento
meu_set.discard(2)
print('Remocao', meu_set)

# Operacoes Matematicas sobre conjuntos Uniao
uniao = meu_set | meu_set2
print(uniao)

# Intercessao
meu_set3 = {1, 2, 3, 4}
meu_set4 = {1, 2, 7, 8, 10}
intercessao = meu_set3 & meu_set4
print(intercessao)
