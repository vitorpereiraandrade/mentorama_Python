# Variavel Local
def variaveis():
    var = 5
    print(var)

print('O valor da veriavel local é:')
variaveis()

# Variavel global
var = 'Algum valor'
print(f'O valor da variável global é:\n {var}')
print('O valor da variavel global é:\n',var) # Outra forma

# Definindo uma funcao com String
def hello(meu_nome):
    print('Ola', meu_nome)
hello('Vitor')
hello('Magaly')
hello('Vini')

# Definindo uma funcao que soma dois numeros
def soma(a, b):
    print(a + b)
soma(2,5)
soma(0,4)
soma(-1,9)
soma(1.5,2.8)

# Definindo uma funcao que soma dois numeros com o print fora da funcao
def soma(a, b):
    soma = a + b
    return soma
    # return(a+b)
print(soma(2,8))

# Retornando se o valor é par ou nao
def epar(x):
    return(x % 2 == 0)
print(epar(2))
print(epar(3))
print(epar(-2))

# Reutilizando a funcao é par em outra funcao
def epar(x):
    return(x % 2 == 0)
def par_ou_impar(x):
    if epar(x):
        return 'par'
    else:
        return 'impar'
print(par_ou_impar(3))
print(par_ou_impar(4))
print(par_ou_impar(7))

# FUNCAO RANGE E LEN
# Funcao que imprime valores de 0 a 9 (10 valores)
var = range(10)
for n in var:
    print(n)

# Funcao Len  retorna o tamanho do vetor / matriz
tam_var = len(var)
print('O tamanho da variavel é:', tam_var)

# FUNCAO LAMBDA
# Funcao Lambda que recebe um valor e retorna o dobro dele (*2)
a = lambda x: x * 2
print(a(3))
print(a(4))

# Funcao Lambda que recebe mais um parametro
aumento = lambda a, b: (a*b/100)
print(aumento(100,5))
print(aumento(1000,10))
