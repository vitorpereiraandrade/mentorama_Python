# CRIEI O INPUT PRA GERAR O ERRO

try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    r = (5 * a) * (3 * b)

except:
    print('Digite um número inteiro')
else:
    print(f'O resultado é {r}')
finally:
    print('Obrigado')

