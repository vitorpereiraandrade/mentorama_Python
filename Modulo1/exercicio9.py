palavra = ('mentorama',)

print(palavra.upper())

print(palavra[::-1])


for p in palavra:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end='')