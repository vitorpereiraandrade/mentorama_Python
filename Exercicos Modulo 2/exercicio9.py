import collections

letras = []
numeros = []
digitos = [0,1,2,3,4,5,6,7,8,9]
lista = ['E',7,'T',8,'K',5,'C',0,'M',9]

for i in lista:
    if i in digitos:
        numeros.append(i)
    else:
        letras.append(i)
numeros.reverse()
total = letras + numeros
print(total)


