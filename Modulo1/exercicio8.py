import math

a = 1
b = 5
c = 6

def bhaskara(a ,b ,c):
    delta = (b ** 2) - 4 * a * c
    print(f'O valor de Delta: {delta:.1f}')
    if a == 0:
        print('Valor de A deve ser difente de 0')
    elif delta < 0:
        print('Sem raiz real')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'x1 = {x1:.1f} e x2 = {x2:.1f}')
raiz = bhaskara(a, b, c)
print(raiz)



