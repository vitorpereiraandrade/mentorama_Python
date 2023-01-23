# CRIEI O INPUT PRA GERAR O ERRO

try:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    c = int(input('Digite o terceiro valor: '))
    soma = a + b + c
except:
    print('Digite números inteiros')
else:
    print(f'A soma das variaveis a, b e c é {soma}')
finally:
    print('Obrigado')






