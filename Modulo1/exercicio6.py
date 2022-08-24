contador = 0
contador2 = 0
lista_par = []
lista_impar = []
for n in range(1, 10):
    if n%2 == 0:
        lista_par.append(n)
        contador += 1
        print(n, end=', ')
print('há', contador, 'números pares de 1 a 10.', 'A soma desse numeros é:', sum(lista_par))
for n in range(1, 11):
    if n%2 == 1:
        lista_impar.append(n)
        contador2 += 1
        print(n, end=', ')
print('há', contador2, 'números impares de 1 a 10.', 'A soma desse numeros é:', sum(lista_impar))
